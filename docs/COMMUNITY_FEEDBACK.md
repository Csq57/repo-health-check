# Community feedback and genuine adoption evidence

This project aims to collect **useful, voluntary, real feedback**, not to manufacture activity for an application.

## Channels

- [Public Issues](https://github.com/Csq57/repo-health-check/issues/new/choose): the bug, feature-request and first-hand usage template **files are merged into `main`**. The public Issue chooser was confirmed to display all three forms in a maintainer-provided screenshot on 23 October 2026; availability may change.
- [Pull requests](https://github.com/Csq57/repo-health-check/pulls): focus on one issue, include tests and limitations.
- [Private vulnerability reports](https://github.com/Csq57/repo-health-check/security/advisories): choose **Report a vulnerability**. Do not paste security details into a public Issue.

## Privacy

By default the CLI's JSON `root` field contains the absolute local directory. Use `--redact-root` to set it to `null` (or display `[redacted]` in text output) before sharing diagnostics. This does **not** anonymize every filename, shell command, captured log or other project identity; still review shared output manually. Never include secrets, account data or customer code. Feedback requires neither contact details nor private repository access.

## Evidence standards

For any future Codex for Open Source application, keep a dated ledger of **verifiable events**: independent user reports, accepted PRs, public mentions, reproducible bug fixes and releases, each with a genuine URL when available. An Issue created by a maintainer for project planning must **not** be counted as external adoption. GitHub Stars and forks alone do not prove active users. Do not invent users, testimonials, downloads or usage figures, or exchange rewards for stars.

**Baseline on 21 October 2026:** public MIT repository, enabled Issues and private reporting; no verified third-party Issues, PRs, releases or adoption was found. Lack of visible evidence is not proof that nobody has ever used the tool.

## Triage

For each real report, maintainers may verify reproduction, label the issue, acknowledge what is known and unknown, and link any later fix and actual CI evidence. Keep third-party feedback attributable only where the reporter chooses to make it public. There is no guaranteed support response time.
