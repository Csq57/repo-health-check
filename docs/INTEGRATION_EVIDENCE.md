# Cross-repository integration evidence (maintainer-run)

**Recorded on:** 23 October 2026 (Sydney). **Status:** source-only, experimental. These checks were executed by the repository owner. **No independent adoption or external maintainer endorsement is claimed.**

## Test A: Read-only inventory against an established public Python project

- Target project: [PyPA Packaging](https://github.com/pypa/packaging), public upstream source at **commit `c1d2a9d8f5ca7cc11b7d2e902ed5ee3e255e8560`**.
- Target was only checked out into a temporary GitHub Actions workspace; no changes or PRs were made to the PyPA repository.
- Scanner: `Csq57/repo-health-check` at **commit `da5d2ad23f9c72b2c5d9f1032c3eb4057129ec2e`** (the squash merge of [PR #5](https://github.com/Csq57/repo-health-check/pull/5)).
- Test runner: GitHub-hosted Ubuntu; Python 3.12; `--format json --redact-root --fail-on warning`.
- Actual outcome: [GitHub Actions run 39920579372](https://github.com/Csq57/ai-python-repository-stabilization-case-study/actions/runs/39920579372) completed **success**. Job logs show `"root": null`, `"warning_count": 0` and no strict-mode failure.
- Reproducible workflow: [read the exact workflow at commit `4939736`](https://github.com/Csq57/ai-python-repository-stabilization-case-study/blob/493973619b31fcf586dfe0e1baef3164e4f63668/.github/workflows/repo-health-public-fixture.yml).

## Test B: Cross-repository warning-gate behavior on a maintainer-owned sample

- Target project: [sanitized case-study repository](https://github.com/Csq57/ai-python-repository-stabilization-case-study), a **different repository owned by the same maintainer**, not an independent user.
- Same pinned scanner commit, GitHub-hosted Ubuntu and Python 3.12.
- Actual outcome: [GitHub Actions run 39901016838](https://github.com/Csq57/ai-python-repository-stabilization-case-study/actions/runs/39901016838) completed **success** with `warning_count: 2` in non-strict mode. With `fail-on: warning`, the Action exited **1 as expected**. The workflow explicitly captured and asserted that expected failure before succeeding overall.
- Reproducible workflow: [read the exact workflow at commit `f4a4e65`](https://github.com/Csq57/ai-python-repository-stabilization-case-study/blob/f4a4e65926a744534b06601c0895b91cac2bc6e0/.github/workflows/repo-health-action-consumer-smoke.yml).

## What these checks do — and do not — prove

These checks demonstrate that the Action can be called from a different repository, that root-path redaction works for the reported scan root, and that strict warning exit handling can be asserted in CI. They do **not** prove that external users adopted the Action, that a Python project is secure, that tests actually pass, that licensing is valid, or that OpenAI has approved the maintainer for its programmes.

The repository's published `v0.1.0` tag predates the Action and remains unchanged. Do not reference `@v0.1.0` for the Action. The linked scanner commit above is intentionally pinned; review changes before upgrading to later commits or a future tagged release.

## How to provide independent feedback

If you **personally** test the Action on a repository you are authorized to access, please use the [public first-hand usage form](https://github.com/Csq57/repo-health-check/issues/new/choose) or file a reproducible bug report. Include platform, Python version, expected/actual results, and a sanitized minimal fixture. No star, testimonial, private code or contact details are required. Do not post credentials, local absolute paths, proprietary files, or private security findings. The `--redact-root` option is **not** a general anonymization guarantee: review all outputs before sharing.

Any real external usage, feedback, review, or merged external contribution should be recorded **only after** verifiable independent evidence is available. Maintainer-run CI tests are not counted as third-party adoption.
