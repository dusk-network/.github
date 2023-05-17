# Default workflows

This workflows directory contains the most commonly used workflow jobs within our organization. These workflows are reusable and can be imported into other workflow files. For more information see the Github article on [Reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).

Example:
```yaml
on: [pull_request, push]

name: Dusk CI

jobs:
  # Import the localized workflow
  analyze:
    name: Code Analysis
    uses: ./.github/workflows/code-analysis.yml

  # It's possible to import workflows from elsewhere
  # that have been marked as `on: workflow_call:`
  test:
    name: Nightly tests
    uses: https://github.com/dusk-network/.github/.github/workflows/nightly-test.yml

  # It's still possible to introduce your own jobs if
  # the workflows specified above do not fit your repos
  # complexities.
  test_nightly_no_std:
      name: Nightly tests no_std
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - uses: dtolnay/rust-toolchain@nightly
          with:
            components: clippy
        - uses: Swatinem/rust-cache@v2
        - run: cargo test --release --no-default-features

```
