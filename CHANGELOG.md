# Changelog

## Unreleased — privacy-friendly output enhancement (pending review)

- Add opt-in `--redact-root` to hide the absolute scan root in JSON/text output and validation errors without changing default behaviour.
- Add three regression tests covering JSON, text/strict exit, and invalid paths, bringing the suite to 12 cases.

## Initial public source baseline — 21 October 2026 (no tagged release)

- Extracted a read-only Python repository maintenance inventory and 9 unit tests from the scoped-MIT material prepared in [case-study PR #1](https://github.com/Csq57/ai-python-repository-stabilization-case-study/pull/1).
- Uses Python standard library only at runtime; CI verifies Python 3.11 and 3.12.
- Introduced a top-level MIT licence, limited exclusively to this independently assembled repository content.

**No tagged release, installation counts, external contributors or independent users are claimed.**
