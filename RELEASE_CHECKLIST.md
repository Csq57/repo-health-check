# v0.1.0 preview release readiness — preparation only

**Historical checkpoint (23 October 2026):** publishing still requires separate owner approval. This is an evidence checklist, not a live status indicator or authorization to create a tag, GitHub Release, package, announcement or OpenAI application. See [Releases](https://github.com/Csq57/repo-health-check/releases) for the current status. Proposed version: `v0.1.0` as a **pre-release**, with source archives only and no PyPI package or wheel.

## Completed and independently confirmed

- [x] Public standalone MIT repository: [Csq57/repo-health-check](https://github.com/Csq57/repo-health-check), with no private OpenTrendIQ source or case-study assets included; see [provenance](docs/PROVENANCE.md). This is an engineering check, not a legal opinion.
- [x] Maintainer-approved public repository and scoped MIT licence, with contributions and security-reporting guidance.
- [x] Root `main` at `abdb3f097e86d603ad8210c2b92c049fdebda946` contained merged [PR #2](https://github.com/Csq57/repo-health-check/pull/2) and release-preparation [PR #3](https://github.com/Csq57/repo-health-check/pull/3) as of 23 October 2026.
- [x] [Main-branch GitHub Actions](https://github.com/Csq57/repo-health-check/actions/runs/39891910968) completed successfully on Python 3.11 and Python 3.12, with 12 unit tests per environment at that preparation baseline.
- [x] `SHA256_MANIFEST.json` matched **18/18** referenced files at that merged preparation snapshot. The manifest intentionally excludes itself.
- [x] Community feedback template files were merged into `main` by [PR #1](https://github.com/Csq57/repo-health-check/pull/1); private vulnerability reporting was enabled and confirmed in authenticated GitHub settings on 21 October 2026.

## Must complete before any public release

- [x] Review and merge the release-preparation documentation through [PR #3](https://github.com/Csq57/repo-health-check/pull/3), and read back the merged source tree. Recheck every later release-target change.
- [x] Verify GitHub Actions on the [merged PR #3 baseline](https://github.com/Csq57/repo-health-check/actions/runs/39891910968), Python 3.11/3.12 individually. Reverify checks on any later final release-tag commit.
- [x] Verify the *public* [Issue chooser](https://github.com/Csq57/repo-health-check/issues/new/choose) renders Bug report, Feature request and First-hand usage feedback (maintainer screenshot, 23 October 2026).
- [ ] Recheck the current public licence, provenance, security settings and links; check release notes against actual behaviour. Avoid statements of independent adoption without dated third-party evidence.
- [x] Verify absence of `v0.1.0` tag and GitHub Releases at the 23 October 2026 preparation checkpoint; **repeat immediately before publication**, pin the exact approved commit and verify its manifest.
- [ ] Obtain explicit **separate owner approval** for the release title, exact tag/commit, pre-release designation and publication. Never treat branch preparation or a PR merge as permission to publish.

## Only after separate publication approval

- [ ] Create or select the GitHub tag on the approved commit and publish the GitHub pre-release using [draft release notes](docs/RELEASE_NOTES_v0.1.0_DRAFT.md), removing all draft-only disclaimers from the public announcement.
- [ ] Read back the published release URL, tag target, archive links, licensing and GitHub Actions status; log the exact publication date and any failures or rollback limitations.
- [ ] Seek voluntary, real user feedback; do not manufacture stars, downloads, testimonials, contributors or eligibility signals for Codex for Open Source.

**Historical preparation:** the checklist did not itself create a release or tag. Consult [GitHub Releases](https://github.com/Csq57/repo-health-check/releases) for current status. Do not claim independent adoption without third-party evidence.
