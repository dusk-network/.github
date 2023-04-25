# Contributing to Dusk Network

:balloon: Thanks for your help improving the project! We are so happy to have you!

There are opportunities to contribute to Dusk Network at any level. It doesn't matter if you are just getting started with Rust, Go or Sveltejs, or are the most weathered expert, we can use your help.

**No contribution is too small and all contributions are valued.**

## Conduct

All projects within the Dusk Network organisation adhere to the [Code of Conduct](./CODE_OF_CONDUCT.md). This describes the _minimum_ behavior expected from all contributors.

## Contributing

At Dusk Network we work with GitHub issue trackers. Every activity, be it a software contribution or a task of different nature that produces a concrete deliverable, is logged in a specific GitHub Issue and handled accordingly. Issues are repo specific.

👉 **Always create and work on GitHub issues**

For any issue, there are fundamentally three ways an individual can contribute:

1. By opening the issue for discussion: For instance, if you believe that you have uncovered a bug in a crate, creating a new issue in the appropriate repo's [issue tracker][issues] is the way to report it.
2. By helping to triage the issue: This can be done by providing supporting details (a test case that demonstrates a bug), providing suggestions on how to address the issue, or ensuring that the issue is tagged correctly.
3. By helping to resolve the issue: Typically this is done either in the form of demonstrating that the issue reported is not a problem after all, or more often, by opening a Pull Request that changes some bit of something in Tokio in a concrete and reviewable manner.

**Anybody can participate in any stage of contribution**. We urge you to participate in the discussion around bugs and participate in reviewing PRs.

### Asking for General Help

If you have reviewed existing documentation and still have questions or are having problems, you can open an issue asking for help.

In exchange for receiving help, we ask that you contribute back a documentation PR that helps others avoid the problems that you encountered.

### Submitting a new Issue

When opening a new issue in the repository's issue tracker, users will be presented with different templates that should be filled in. Following are the issue templates that one should follow:

- [Bug Report](../.github/ISSUE_TEMPLATE/bug_report.md): Use this template for reporting problems related to existing code that does not do what it is intended.
- [Feature Request](../.github/ISSUE_TEMPLATE/feature_request.md): Use this template for requesting the development of code not yet existing, either to create new functionalities, or to modify existing ones.
- [Specification Request](../.github/ISSUE_TEMPLATE/specs.md): Use this template for requesting the creation of documentation to specify new or existing features.

Do not worry if you cannot answer every detail in the template, just fill in what you can.

The two most important pieces of information we need in order to properly evaluate the report is a description of the behavior you are seeing and a simple test case we can use to recreate the problem on our own. If we cannot recreate the issue, it becomes impossible for us to fix.

In order to rule out the possibility of bugs introduced by userland code, test cases should be limited, as much as possible, to using only Tokio APIs.

See [How to create a Minimal, Complete, and Verifiable example](https://stackoverflow.com/help/minimal-reproducible-example).

## Resolving Issues

### Work on a feature branch

If you are working on an issue, you should work on a **feature branch**. Call the feature branch in a way that it clearly points to the issue it refers to (`feature-[issue_nr]` is a safe choice). Also, make sure to push your feature branch to the `remote` repository.

### Commits

It is a recommended best practice to keep your changes as logically grouped as possible within individual commits. There is no limit to the number of commits any single Pull Request may have, and many contributors find it easier to review changes that are split across multiple commits.

That said, if you have a number of commits that are "checkpoints" and don't represent a single logical change, please squash those together.

Note that multiple commits often get squashed when they are landed (see the notes about [commit squashing](#commit-squashing)).

#### 👉 Commit message guidelines

A good commit message should describe what changed and why.

> 💡 The commit message structure has been inspired by this [great article of Chris Beam over the importance of keeping a clean commit message history](https://chris.beams.io/posts/git-commit/). Make sure to read it!

1. The first line should:

   * Be capitalised.
   * Provide a short description of the change in 50 characters or less, and no more than 72 characters.
   * Have no period at the end of the line.
   * Use the imperative mood.
   * Be entirely in lowercase with the exception of proper nouns, acronyms, and the words that refer to code, like function/variable names.
   * Focus on the problem that this commit is solving in terms of **why** you are making this change rather than ~~how~~

2. Keep the second line blank.

3. Wrap all other lines at 72 columns (except for long URLs). Bullet points are fine (typically a hyphen or asterisk is used for the bullet preceded by a single space, with blank lines in between)

4. If your patch fixes an open issue, you can add a reference to it at the end of the log. Use the `Fixes: #` or `Resolves: #`  prefix and the issue number. For other references use `See also: #`, which may include multiple issues, separated by a comma.

   Examples:

   - `Fixes #1337`
   - `See also #1234, #5678`

**Sample Complete Commit Message**

```txt
# Summarize changes in around 50 characters or less
#
# Capitalize the subject line
# Do not end the subject line with a period
# Use the imperative mood in the subject line
# Separate subject from optional body with a blank line
# Wrap the body at 72 characters
# Explain the problem that this commit is solving. Focus on "why" you
# are making this change as opposed to "how" (the code explains that).
#
# Further paragraphs come after blank lines.
#
#  - Bullet points are okay, too
#
#  - Typically a hyphen or asterisk is used for the bullet, preceded
#    by a single space, with blank lines in between
#
# If you use an issue tracker, put references to them at the bottom:
#
# Resolves #123
# See also #456, #789
```

## Pull Request Lifecycle

Issues are always resolved by opening a Pull Request. **Don't close an issue by pushing your commits directly to the `main` branch!** 

The process for opening and reviewing a Pull Request is similar to that of opening and triaging issues, but carries with it a necessary review and approval workflow that ensures that the proposed changes meet the minimal quality and functional guidelines of Dusk Network.

### 👉 Open a Draft PR ASAP 

In order for people to prevent or help clearing out blockers as soon as possible, it is paramount for them to be familiar with and able to follow the code under development. This is impossible if PRs are created as a last step before pushing commits.

Therefore, **as soon as you create the feature branch, it is good practice to open a PR in `Draft`**.

Pushing on the `Draft`  PR should happen frequently. Do not fear to push commits with failing tests and even not building. That is what `git rebase` is for.

Other than that, please follow these guidelines in handling your PRs:

- Keep your PRs in`Draft` until they are ready to be reviewed.
- Be descriptive in the titles of your PRs and also provide good descriptions about which things are being added, changed, fixed or removed also addressing the corresponding issue that it is addressing to.
- Any pull request that is not passing our CI tests & builds will not be merged. This implies incorrect formatting errors, compilation errors, clippy lints, or any other kind of inconsistency with your code.
- Do not open PRs that are not linked or related to a previously opened issue.
- Update the `Unreleased` section of the `CHANGELOG` if your PR includes anything that's worth mentioning in there. Avoid adding things like doc-nitpicks and similar changes which do not affect directly any added, fixed, removed or changed feature.

### Set PR To Ready For Review

When you are done with your PR, change it from _draft_ to _ready for review._ 

PR ready for reviews should be cleared as soon as possible. Make sure to **mention** reviewers on IM when your PR is ready for review, or you are done with reviewing one. 

Pull Requests are the way concrete changes are made to the code, documentation, and dependencies in the various repositories of Dusk Network. Even tiny pull requests (e.g., one character pull request fixing a typo in API documentation) are greatly appreciated. Before making a large change, it is usually a good idea to first open an issue describing the change to solicit feedback and guidance. This will increase the likelihood of the PR getting merged.

### Tests

If the change being proposed alters code (as opposed to only documentation for example), it is either adding new functionality to a crate or it is fixing existing, broken functionality. In both of these cases, the pull request should include one or more tests to ensure that the crate does not regress in the future. There are two ways to write tests: integration tests and documentation tests (we strive to avoid unit tests as much as possible).

#### Integration tests

Integration tests go in the same space as the code they are testing. For `rust` repositories, this is the crate (in which case each sub crate should have a `dev-dependency` on the main crate itself. This makes all utilities available to use in tests, no matter the crate being tested).

The best strategy for writing a new integration test is to look at existing integration tests in the crate and follow the style.

#### Documentation tests

Ideally, every API has at least one [documentation test] that demonstrates how to use the API. In `rust`, documentation tests are run with `cargo test --doc`. This ensures that the example is correct and provides additional test coverage.

The trick to documentation tests is striking a balance between being succinct for a reader to understand and actually testing the API.

The type level example for `tokio_timer::Timeout` provides a good example of a documentation test:

```rust
/// // import the `timeout` function, usually this is done
/// // with `use tokio::prelude::*`
/// use tokio::prelude::FutureExt;
/// use futures::Stream;
/// use futures::sync::mpsc;
/// use std::time::Duration;
///
/// # fn main() {
/// let (tx, rx) = mpsc::unbounded();
/// # tx.unbounded_send(()).unwrap();
/// # drop(tx);
///
/// let process = rx.for_each(|item| {
///     // do something with `item`
/// # drop(item);
/// # Ok(())
/// });
///
/// # tokio::runtime::current_thread::block_on_all(
/// // Wrap the future with a `Timeout` set to expire in 10 milliseconds.
/// process.timeout(Duration::from_millis(10))
/// # ).unwrap();
/// # }
```

Given that this is a *type* level documentation test and the primary way users of `tokio` will create an instance of `Timeout` is by using `FutureExt::timeout`, this is how the documentation test is structured.

Lines that start with `/// #` are removed when the documentation is generated. They are only there to get the test to run. The `block_on_all` function is the easiest way to execute a future from a test. If this were a documentation test for the `Timeout::new` function, then the example would explicitly use `Timeout::new`. For example:

```rust
/// use tokio::timer::Timeout;
/// use futures::Future;
/// use futures::sync::oneshot;
/// use std::time::Duration;
///
/// # fn main() {
/// let (tx, rx) = oneshot::channel();
/// # tx.send(()).unwrap();
///
/// # tokio::runtime::current_thread::block_on_all(
/// // Wrap the future with a `Timeout` set to expire in 10 milliseconds.
/// Timeout::new(rx, Duration::from_millis(10))
/// # ).unwrap();
/// # }
```

### Discuss and update

You will probably get feedback or requests for changes to your Pull Request. This is a big part of the submission process so don't be discouraged! Some contributors may sign off on the Pull Request right away, others may have
more detailed comments or feedback. This is a necessary part of the process in order to evaluate whether the changes are correct and necessary.

**Any community member can review a PR and you might get conflicting feedback**.
Keep an eye out for comments from code owners to provide guidance on conflicting feedback.

**Once the PR is open, do not rebase the commits**. See [Commit Squashing](#commit-squashing) for more details.

### Commit Squashing

When a PR is in `Draft` it is possible to squash the commits in the PR to make the job of the reviewer easier (as long as the commits follow the [Commits](#Commits) guideline). 

After moving the PR out of the `Draft` stage, **avoid squashing commits, including those that you add to your Pull Request during the review process**. When the commits in your Pull Request land, they may be squashed into one commit per logical change. Metadata can be added to the commit message (including links to the PR, links to relevant issues, and the names of the reviewers). The commit history of your PR, however, will stay intact on the PR page.
