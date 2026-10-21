# Contributing

This is an experimental, standalone Python inventory. It uses Python 3.11+ and standard-library-only runtime code.

1. Reproduce the issue on a clean checkout, ideally with a minimal fictional fixture. Never upload customer repositories, tokens or nonpublic financial data.
2. Describe the actual behaviour, expected behaviour, Python version and platform.
3. Add a regression test that fails before the fix and passes afterward.
4. Keep changes narrow and preserve the tool's read-only contract. Do not add network access or code execution without a separate design review.
5. Run `python -m unittest discover -s tests -p 'test_repo_health_check.py' -v` before proposing changes.

**Status:** the [public GitHub repository](https://github.com/Csq57/repo-health-check) exists, with an [issue tracker](https://github.com/Csq57/repo-health-check/issues) for non-sensitive reports. No external contribution, download or adoption claims have been verified.
