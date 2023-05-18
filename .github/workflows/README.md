# Default workflows

This workflows directory contains the most commonly used workflow jobs within our organization. These workflows are reusable and can be imported into other workflow files. For more information see the Github article on [Reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).

Example:
```yaml
on: [pull_request, push]

name: Dusk CI

jobs:
  # Import the reusable workflow to use Clippy and Rustfmt
  code_analysis:
    name: Code Analysis
    uses: dusk-network/.github/.github/workflows/code-analysis.yml@main

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

To set the toolchain for the workflows, specify a `rust-toolchain` or `rust-toolchain.toml` file.
