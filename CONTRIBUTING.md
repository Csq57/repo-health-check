# Contributing

Repo Health Inventory is an experimental Python 3.11+ project with zero third-party runtime dependencies. Contributions should preserve the **read-only, no-target-code-execution, no-network** contract.

Choose the appropriate route through [GitHub's Issue chooser](https://github.com/Csq57/repo-health-check/issues/new/choose):

- **Bug:** include Python version, OS, reproducible fictional directory, expected and observed outputs; redact local paths.
- **Feature:** describe a real maintenance need, bounded implementation and alternatives.
- **First-hand feedback:** optionally describe your actual use and what was confusing; no testimonial, star or private repository access is required.
- **Security vulnerability:** do **not** open a public Issue; use the private channel in [SECURITY.md](SECURITY.md).

To submit a code change:

1. Reproduce the issue using synthetic data, not a customer repository or secret.
2. Keep the change small and protect existing CLI behaviour.
3. Add tests for behavioural changes.
4. Run `python -m unittest discover -s tests -p 'test_repo_health_check.py' -v`, and report the actual result.
5. Open a PR documenting limitations. Do not claim a test passed when it was not run.

See [community feedback and evidence policy](docs/COMMUNITY_FEEDBACK.md). No externally validated user adoption or independent contribution is claimed at this stage.
