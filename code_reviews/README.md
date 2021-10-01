# Code Reviews

## It is all about improving communication

The main reason to do code reviews is to **develop the discipline to argument your code to your other team members**. If done well, code reviews ultimately lead to better code, more distributed ownership, and healthy debate.

Bugs should be caught through testing, so while the review can occasionally pinpoint problems, debugging is not the main reason to have code reviews.

Code reviews should be an occasion to promote:

- Knowledge Transfer
- Increased Team Awareness
- Finding Alternative Solutions
- Catching inaccuracies
- Ensuring consistency (especially in interface and APIs)

## As an author

First and foremost, try and follow the guidelines about [contributing to the code base](/development/README.md#contributing).

### Provide two paragraphs of context in your PR

Providing sufficient context other than a simple *Fixes #bla,* make it valuable for a reviewer to review the code, and will make the reviewer pay more attention. As painful that it might sound, it will help accomplish the above points much faster.

## As a reviewer

### Celebrate good code

It is important to provide positive reinforcement for a job well done. This can also be extended on how the PR is structured.

### Ask, don't tell

Asking questions promotes conversations. Making demands cut the conversations short. Consider beginning your comment with "*Have you considered...?"* or "*Can you clarify...?"*

Sometimes even questions can lead to negativity bias, which should be avoided. Bad question examples are *"Why didn't you just..."*

## What to check in a review

### Time to completion

If a review is taking more than 10 minutes, the code change is too broad. This means that the issue should have been broken down and produce multiple PRs. Small changes are also easier to provide context on.

### Single responsibility principle

Does every object, function, component in the system does only have one job?

### Naming

Good names makes it easier to discuss.

### Complexity

Ask for clarification. If the tradeoff is *more complexity in exchange for future opportunities*, this is probably an occasion for tackling the future opportunity to a new, dedicated issue, and cut down on the complexity part.

### Test Coverage

We are not checking for bugs, but we can definitely check if the tests cover enough of the changes.

### Code smells

Code “smells” are indicators that something may be wrong. They are useful because they are easier to see than the root cause of a problem. Share your best refactoring ideas with the committer and be open to ignore them (sometimes, fixing code smells can lead to problems and we need to strive for a good balance).

### Adherence to Style Guide

Please refer to [this guideline](https://github.com/dusk-network/org/blob/master/CONTRIBUTING.md) for the correct commit message outline. Also, check if the commit message is readable and if it contains breaking changes.

### Whatever your expertise lies

Ergonomic APIs, code duplication, performance (when not premature), security. Feel free to expand the review checklist with anything you think you know well.

## Conflict Resolution

### Disagreement about issues

When leading to a healthy confrontation and learning moment, conflicts are good. However, we don't have the luxury to engage in endless debates, so **at some point we need to agree to disagree**.

To help reaching a conclusion in case of disagreement, the reviewer must honestly answer the question "*is the minimum bar for quality reached here or I simply would have done the task differently?*".

### Disagreement about process

A few examples are working without opening issues, not structuring the issues with the right template, not write documentation, pushing directly to master, opening pull requests and ignoring feedback, etc.

When these things happen, get in front of it and check if the process is too heavy and needs changes. If the team agrees, apply those changes. Otherwise, do the review anyway and ask questions to the committer and ask him/her to follow the guidelines.

If the process still gets ignored, then revert the code, put it in a PR, have the committer structure the issue and the PR according to the rules, and only then do the review and accept the changes.

