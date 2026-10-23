# Changelog

## Unreleased — proposed v0.1.0 preview (not tagged or published)

This is the first proposed GitHub preview release of Repo Health Inventory, a standard-library-only, read-only Python 3.11+ command-line maintenance inventory.

- Report the presence of a README, explicit licence, GitHub Actions workflow, Python test module and optional packaging, contribution and security files.
- Provide text and JSON output, with strict `--fail-on warning` exit behaviour for automation.
- Bound file discovery at 20,000 files / 5,000 directories; report incomplete scans rather than falsely claiming tests are absent.
- Add opt-in `--redact-root` for JSON/text output and invalid-root error messages without changing default CLI behaviour.
- Include 12 Python `unittest` cases and SHA-256 records for tracked repository files.
- Document MIT scope, safety boundaries and the appropriate channels for public feedback or private vulnerability reports.

**Verified:** on the merged `main` commit `ac4c193a87a72995d2a87a6493a37e306a41711e`, [GitHub Actions](https://github.com/Csq57/repo-health-check/actions/runs/39803356195) passed on Python 3.11 and 3.12. The proposed release-preparation documentation itself remains to be validated after integration.

**Not provided:** a PyPI distribution, wheel, code-execution audit, vulnerability scanner, security certification, service-level agreement or release assets beyond GitHub's automatic source archives if a release is later published.

See the [draft release notes](docs/RELEASE_NOTES_v0.1.0_DRAFT.md) for the proposed announcement and limitations.

## Historical source baseline — 21 October 2026 (not a tagged release)

- Established the public standalone repository from the scoped-MIT [case-study PR #1](https://github.com/Csq57/ai-python-repository-stabilization-case-study/pull/1), initially with 9 tests.
- Added community contribution templates and private vulnerability reporting guidance.
- [PR #2](https://github.com/Csq57/repo-health-check/pull/2) subsequently merged the privacy flag, three regression tests and updated file-integrity manifest on 23 October 2026 (Sydney time).

**No tag, published release, download count, external contributor or independent user adoption is claimed as of this candidate preparation.**
