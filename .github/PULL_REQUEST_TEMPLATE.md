## Summary and purpose
<!-- Describe the real problem, the bounded change and expected benefit. -->

## Safety
- [ ] The read-only and no-target-code-execution boundary is preserved
- [ ] No network calls, credentials, private repository data or sensitive paths are introduced
- [ ] Changes are restricted to the documented scope

## Verification
- [ ] Ran `python -m unittest discover -s tests -p 'test_repo_health_check.py' -v`
- [ ] Added a regression test for behaviour changes, or explained why not
- [ ] Checked the CLI output and documentation

## Limitations
<!-- Public PRs must not disclose vulnerabilities; use private reporting instead. -->
