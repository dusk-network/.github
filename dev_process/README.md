# Development Guidelines

## WorkFlow

### Always Create And Work On GH Issues

Creating issues on Github before working on code is obligatory and a prerequisite for all other points

### Create Draft PR First

The first action when working on some issue, is to create a draft PR for all other team members to follow.

In order for people to prevent or help clearing out blockers as soon as possible, it is paramount for them to be familiar and be able to follow the code under development. This is impossible if PRs are created as a last step before pushing commits. 

#### Push On Draft PR Frequently

Intimately related to the previous point, commits on the draft PR must happen frequently. Do not fear to commit code with failing tests and even not building. That is what `git rebase` is for. 

It is common to be tempted to first verify assumptions about a problem on your own, and only then tell your teammates about where the problem is. _Don't!_ It is much more productive to communicate your suspicions first, and then verify them.

{% hint style="warning" %}
Sometimes it might not be possible to push frequently \(i.e. when someone's debugging\). In this case, make sure to add comments to your PR with your findings
{% endhint %}

### Set PR Ready For Review

When you are done with your PR, chage it from _draft_ to _ready for review._ 

PR ready for reviews should be cleared as soon as possible. Make sure to **mention** reviewers on IM when your PR is ready for review, or you are done with reviewing one. 

## Priority

Priorities is set on the board. However, some items should always be prioritized before the others. From a general perspective, following priority list is always valid

1. [Blockers](development-guidelines.md#blockers-and-how-to-deal-with-them)
2. [PR Reviews](development-guidelines.md#pr-reviews)
3. Other issues     &lt;--- These items are normally the object of planning

### Blockers \(and how to deal with them\)

Some would argue that blockers in software development are more linked to perception, than code. When developing, the whole core of a program is by definition a blocker for the business, whether we are talking about a library, a service, a process or a dependency. Therefore, when we talk about blockers, we actually point to a variety of different root causes, which all have to do with the **perceived incapability of clearing out issues** directly.

If you are working on something, by definition you are not blocked. Therefore, when perceiving blockers, we need to address the incapability of clearing out issues in the parts of the codebase we are not familiar with. 

In order to do that, we need a set of both proactive and reactive measures to avoid blockers \(read: to avoid working on lower priority items, or, worse, fishing for stuff to do\). As usual, many of these measures are directly linked with improving and retaining the quality of communications within the core team.

#### Work Together More

{% hint style="warning" %}
There must be **at least 2 people** clearing out a blocker. Even if there is no way to divide the work, pairing is not possible and they must duplicate their efforts
{% endhint %}

#### Break Blockers Down

Blockers are normally perceived as systemic to a whole deliverable. However, this is seldom the case. By breaking down the blocking issue into smaller unit of works, normally a workaround is found to allow other people to keep working on their tasks. In any case, this helps the rest of the team to understand what's going on, and even help out solving the issue at hand.

#### Screen Sharing ASAP

Normally blockers are reported during a standup. As soon as there is consensus that an issue is a blocker, the developer working on the related issue must share his screen at the end of the standup and explain where the blocker is likely to be. A blocker break down shall happen immediately after.

### PR Reviews

Reviews are higher priority than working on the issues, with the sole exception for blockers. This is to prevent code rotting and other problems. If you are requested to review a PR, you should pause everything else and focus on clearing the PR first. 

## Working Together

### The Overlap

Although everybody can organize the work however they feel more production, there is a time frame when everybody working must be online.

{% hint style="info" %}
Everybody must be online from 11:30 until 12:30 and then from 14.00 until 17.00 \(GMT+1\) during the work week. This time space is called the _Overlap_ 
{% endhint %}

### Communicate Often

Communication is a huge component of a functioning team. When working on an issue perceived as a blocker, you should turn the communication nob up. The work is higher priority anyway, so have a confcall and report frequently on the IM your progress, your ounces, and questions.

#### Share Phone Numbers

Make sure to share your phone number with the other team members and **don't shy away from calling people directly**.

### Mentions Must Be Answered ASAP During Overlap

When addressed on IM with a mention, please answer as soon as you can. During the _Overlap_ the turnaround should not take more than 5 minutes. If you are encumbered or unavailable for whatever reason, please reply with that and setup a suitable time for a call. 
