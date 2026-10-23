# v0.1.0 preview release readiness — preparation only

**State:** DRAFT / NO-GO for publishing. This checklist is not authorization to create a tag, GitHub Release, package, announcement or OpenAI application. Proposed version: `v0.1.0`, marked **pre-release** if later approved. Source distribution only (GitHub-generated ZIP/tarball); there is no installable PyPI package or wheel.

## Completed and independently confirmed

- [x] Public standalone MIT repository: [Csq57/repo-health-check](https://github.com/Csq57/repo-health-check), with no private OpenTrendIQ source or case-study assets included; see [provenance](docs/PROVENANCE.md). This is an engineering check, not a legal opinion.
- [x] Maintainer-approved public repository and scoped MIT licence, with contributions and security-reporting guidance.
- [x] Root `main` at `ac4c193a87a72995d2a87a6493a37e306a41711e` contains the merged [PR #2](https://github.com/Csq57/repo-health-check/pull/2) privacy improvement; `--redact-root` remains opt-in.
- [x] [Main-branch GitHub Actions](https://github.com/Csq57/repo-health-check/actions/runs/39803356195) completed successfully on Python 3.11 and Python 3.12, with 12 unit tests per environment.
- [x] `SHA256_MANIFEST.json` matched **17/17** referenced files at that merged `main` snapshot. The manifest intentionally excludes itself.
- [x] Community feedback template files were merged into `main` by [PR #1](https://github.com/Csq57/repo-health-check/pull/1); private vulnerability reporting was enabled and confirmed in authenticated GitHub settings on 21 October 2026.

## Must complete before any public release

- [ ] Review and merge this release-preparation documentation into `main` through a separate, reviewed change; then read back the final source commit and all file hashes.
- [ ] Re-run GitHub Actions on the final release-candidate `main` and verify Python 3.11/3.12 checks individually rather than assuming a green badge.
- [ ] Verify the *public* [Issue chooser](https://github.com/Csq57/repo-health-check/issues/new/choose) actually renders the bug, feature and firsthand-feedback forms; file presence alone is insufficient.
- [ ] Recheck the current public licence, provenance, security settings and links; check release notes against actual behaviour. Avoid statements of independent adoption without dated third-party evidence.
- [ ] Verify a `v0.1.0` tag and Release do not already exist; pin the exact approved `main` commit for publication and document the matching manifest.
- [ ] Obtain explicit **separate owner approval** for the release title, exact tag/commit, pre-release designation and publication. Never treat branch preparation or a PR merge as permission to publish.

## Only after separate publication approval

- [ ] Create or select the GitHub tag on the approved commit and publish the GitHub pre-release using [draft release notes](docs/RELEASE_NOTES_v0.1.0_DRAFT.md), removing all draft-only disclaimers from the public announcement.
- [ ] Read back the published release URL, tag target, archive links, licensing and GitHub Actions status; log the exact publication date and any failures or rollback limitations.
- [ ] Seek voluntary, real user feedback; do not manufacture stars, downloads, testimonials, contributors or eligibility signals for Codex for Open Source.

**As prepared, no release/tag has been created and no verified independent adoption is claimed.**
