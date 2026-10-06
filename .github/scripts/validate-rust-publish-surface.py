#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def annotation_escape(value):
    return str(value).replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def error(title, message, file=None):
    parts = [f"title={annotation_escape(title)}"]
    if file:
        parts.insert(0, f"file={annotation_escape(file)}")
    print(f"::error {','.join(parts)}::{annotation_escape(message)}")


def validate_relative_file(path_value, label):
    path = Path(path_value)
    if path.is_absolute() or ".." in path.parts:
        error(
            "Invalid manifest path",
            f"{label} must be a relative path inside the repository.",
        )
        return False
    if not path.is_file():
        error("Missing manifest", "Cargo manifest not found.", file=path_value)
        return False
    return True


def find_crates_io_patches(root):
    matches = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            name for name in dirnames if name not in {".git", "target"}
        ]
        if "Cargo.toml" not in filenames:
            continue

        cargo_toml = Path(dirpath) / "Cargo.toml"
        try:
            lines = cargo_toml.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            lines = cargo_toml.read_text(errors="replace").splitlines()

        for line_number, line in enumerate(lines, 1):
            if line.strip() == "[patch.crates-io]":
                matches.append((cargo_toml, line_number))

    return matches


def cargo_metadata(manifest_path):
    command = [
        "cargo",
        "metadata",
        "--no-deps",
        "--format-version",
        "1",
        "--manifest-path",
        manifest_path,
    ]
    completed = subprocess.run(command, check=False, text=True, capture_output=True)
    if completed.returncode != 0:
        if completed.stdout:
            print(completed.stdout, end="")
        if completed.stderr:
            print(completed.stderr, end="", file=sys.stderr)
        error("Cargo metadata failed", f"`{' '.join(command)}` failed.")
        return None
    return json.loads(completed.stdout)


def validate_publish_surface(metadata, publish_packages):
    expected = {name.strip() for name in publish_packages.split(",") if name.strip()}
    expected.discard("__no_publishable_crates__")

    workspace = set(metadata["workspace_members"])
    packages = [
        package for package in metadata["packages"] if package["id"] in workspace
    ]
    by_name = {package["name"]: package for package in packages}
    errors = 0

    missing = expected - set(by_name)
    if missing:
        error(
            "Unknown publish packages",
            f"Not found in cargo metadata: {', '.join(sorted(missing))}",
        )
        errors += 1

    for package in packages:
        name = package["name"]
        manifest = package["manifest_path"]
        publish = package.get("publish")
        manifest_publishable = publish is None or publish != []

        if manifest_publishable and name not in expected:
            error(
                "Unexpected publishable crate",
                f"{name} is publishable in Cargo.toml but not listed in publish-packages",
                file=manifest,
            )
            errors += 1

        if name in expected:
            for field in ("description", "repository", "license"):
                if not package.get(field):
                    error(
                        "Missing package metadata",
                        f"{name} is missing package.{field}",
                        file=manifest,
                    )
                    errors += 1

            for dep in package.get("dependencies", []):
                source = dep.get("source") or ""
                if source.startswith("git+"):
                    error(
                        "Git dependency not publishable",
                        f"{name} depends on git source {source}",
                        file=manifest,
                    )
                    errors += 1

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate the crates.io publish surface for a Rust workspace."
    )
    parser.add_argument("--manifest-path", required=True)
    parser.add_argument("--publish-packages", required=True)
    args = parser.parse_args()

    errors = 0

    if not validate_relative_file(args.manifest_path, "manifest-path"):
        return 1

    for path, line_number in find_crates_io_patches(Path(".")):
        print(f"{path}:{line_number}: [patch.crates-io]")
        errors += 1

    if errors:
        error(
            "Private patch not publishable",
            "Remove [patch.crates-io] before releasing crates.",
        )
        return 1

    metadata = cargo_metadata(args.manifest_path)
    if metadata is None:
        return 1

    errors += validate_publish_surface(metadata, args.publish_packages)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
