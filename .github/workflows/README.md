# Default workflows

This workflows directory contains the most commonly used workflow jobs within our organization. These workflows are reusable and can be imported into other workflow files. For more information see the Github article on [Reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).

By default, the workflows use `core` runners. These are self-hosted runners in a Linux Ubuntu environment. If you run into a `startup failure` error with these runners, be sure to enable the self-hosted runners for the repository and allow external actions to be executed. Repositories can override the default runner label with the reusable workflow `runner` input.

The reusable workflows are configured for least privilege:
- They run with `permissions: contents: read`.
- `actions/checkout` uses `persist-credentials: false`.
- For `pull_request` events, fork PR jobs are blocked on `core` by default. Set `allow_fork_pr_on_core: true` only if you explicitly want to allow that.
- Third-party actions are pinned to immutable commit SHAs.
- Callers should pin reusable workflow refs to immutable commit SHAs instead of mutable branches such as `main`.

Example:
```yaml
on: [pull_request, push]

name: Dusk CI

jobs:
  # Import the reusable workflow to use Clippy and Rustfmt.
  # Rustfmt runs first inside the same job as Clippy, using the toolchain
  # specified in the `rust-toolchain.toml` file.
  #
  # The default clippy configuration might be too strict for certain repositories.
  # The `clippy_default` parameter is set to true and will execute:
  # `cargo clippy --all-features --release -- -D warnings
  #
  # If it is set to false and an empty `clippy_args` argument is passed, 
  # `cargo clippy` will be executed.
  #
  # If arguments are passed with `clippy_args` while `clippy_default` is set to
  # false, `cargo clippy {clippy_args}` will be ran.
  code_analysis:
    name: Code Analysis
    uses: dusk-network/.github/.github/workflows/code-analysis.yml@<full_commit_sha>
  # with:
  #   runner: core
  #   clippy_default: true
  #   clippy_args: ''
  #   enable_sccache: true
  #   allow_fork_pr_on_core: false

  # Import the Dusk analyzer workflow to check for license markings etc.
  #
  # If your project is not in the root directory, pass the `working-directory` input.
  # It is required to have a `rust-toolchain.toml` in the root of your project, regardless
  # of whether you pass a `working-directory` or not. This is due to an underlying action 
  # not allowing for the working directory to be changed for itself.
  dusk_analysis:
    name: Dusk Analyzer
    uses: dusk-network/.github/.github/workflows/dusk-analysis.yml@<full_commit_sha>
    with:
      runner: core
      working-directory: ./app
      # allow_fork_pr_on_core: false

  # Test flags are passable to `run-tests`:
  test_no_std:
    name: no_std tests
    uses: dusk-network/.github/.github/workflows/run-tests.yml@<full_commit_sha>
    with:
      runner: core
      test_flags: --no-default-features
      # enable_sccache: true
      # allow_fork_pr_on_core: false

  # In case the repository needs to enable specific features or requires a Rust target installed:
  test_features:
    name: Specific features tests
    uses: dusk-network/.github/.github/workflows/run-tests.yml@<full_commit_sha>
    with:
      runner: core
      test_flags: --features=feature1,feature2
      rust_target: wasm32-unknown-unknown
      # enable_sccache: true
      # allow_fork_pr_on_core: false

  # Import cargo-deny checks.
  # The selected working directory must contain deny.toml.
  cargo_deny:
    name: Cargo Deny
    uses: dusk-network/.github/.github/workflows/cargo-deny.yml@<full_commit_sha>
    with:
      runner: core
      working-directory: ./app
      deny-check-args: --all-features
      # enable_sccache: true
      # allow_fork_pr_on_core: false

  # Run a reviewed Make target while keeping the shared hardened Rust bootstrap.
  make_target:
    name: Make target
    uses: dusk-network/.github/.github/workflows/run-make.yml@<full_commit_sha>
    with:
      runner: core
      make_target: no-std
      # working-directory: .
      # rust_target: wasm32-unknown-unknown
      # enable_sccache: true
      # allow_fork_pr_on_core: false

```

## Toolchain And Cache

To set the toolchain for the workflows, usage of `rust-toolchain.toml` is recommended. For certain channels, toolchain components like `clippy` and `rustfmt` are not available by default. This is problematic when using the `code_analysis` workflow. The following example config is therefore recommended:
```toml
[toolchain]
channel = "nightly"
components = ["clippy", "rustfmt"]
```

When `enable_sccache` is left at its default value, the reusable Rust workflows automatically set `RUSTC_WRAPPER` if `sccache` is available on the runner and emit `sccache -s` at the end of the job. This keeps cache usage visible without making hosted runners fail if `sccache` is absent.

The `run-make` workflow is intentionally constrained to a single validated Make target. Pass `make_target`, not a shell command string, so repositories can reuse the hardened bootstrap without turning the shared workflow into a generic command runner.
