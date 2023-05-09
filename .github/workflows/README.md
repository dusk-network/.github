# Default workflows

This workflows directory contains the most commonly used workflow jobs within our organization. These workflows are reusable and can be imported into other workflow files. For more information see the Github article on [Reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).

Example:
```yaml
on: [pull_request, push]

name: Dusk CI

jobs:
  analyze:
    name: Code Analysis
    uses: ./.github/workflows/code-analysis.yml

  test:
    name: Nightly tests
    uses: ./.github/workflows/nightly-test.yml

```
