# Default workflows

This workflows directory contains the most commonly used workflow jobs within our organization. These workflows are reusable and can be imported into other workflow files. For more information see the Github article on [Reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).

Example:
```yaml
on: [pull_request, push]

name: Dusk CI

jobs:
  # Import the reusable workflow to use Clippy and Rustfmt
  analyze:
    name: Code Analysis
    uses: dusk-network/.github/.github/workflows/code-analysis.yml@main

  # Import the Dusk analyzer workflow to check for license markings etc.
  analyze:
    name: Dusk Analyzer
    uses: dusk-network/.github/.github/workflows/dusk-analysis.yml@main

  # The `run-tests` workflow has a couple of configuration options.
  # The defaults should be enough to run tests for release and uses
  # the Rust nightly toolchain.
  test_nightly_std:
    name: Nightly release tests
    uses: dusk-network/.github/.github/workflows/run-tests.yml@main

  # The toolchain and test flags are passible though:
  test_stable_no_std:
    name: Stable no_std tests
    uses: dusk-network/.github/.github/workflows/run-tests.yml@main
    with:
      rust_toolchain: stable
      test_flags: --no-default-features

  # In case the repository needs to enable specific features:
  test_nightly_features:
    name: Nightly specific features tests
    uses: dusk-network/.github/.github/workflows/run-tests.yml@main
    with:
      test_flags: --features=feature1,feature2

```
