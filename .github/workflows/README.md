# Default workflows

This workflows directory contains the most commonly used workflow jobs within our organization. These workflows are reusable and can be imported into other workflow files. For more information see the Github article on [Reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).

Example:
```yaml
on: [pull_request, push]

name: Dusk CI

jobs:
  # Import the reusable workflow to use Clippy and Rustfmt
  # Rustfmt is ran with the nightly toolchain by default due to nice features
  # not being stable yet. The toolchain type and version is, however, passable to the 
  # workflow file.
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
    uses: dusk-network/.github/.github/workflows/code-analysis.yml@main
  # with:
  #   toolchain: stable
  #   clippy_default: true
  #   clippy_args: ''

  # Import the Dusk analyzer workflow to check for license markings etc.
  dusk_analysis:
    name: Dusk Analyzer
    uses: dusk-network/.github/.github/workflows/dusk-analysis.yml@main

  # Test flags are passable to `run-tests`:
  test_no_std:
    name: no_std tests
    uses: dusk-network/.github/.github/workflows/run-tests.yml@main
    with:
      test_flags: --no-default-features

  # In case the repository needs to enable specific features:
  test_features:
    name: Specific features tests
    uses: dusk-network/.github/.github/workflows/run-tests.yml@main
    with:
      test_flags: --features=feature1,feature2

```

## Toolchain

To set the toolchain for the workflows, usage of `rust-toolchain.toml` is recommended. For certain channels, toolchain components like `clippy` and `rustfmt` are not available by default. This is problematic when using the `code_analysis` workflow. The following example config is therefore recommended:
```toml
[toolchain]
channel = "nightly"
components = ["clippy", "rustfmt"]
```
