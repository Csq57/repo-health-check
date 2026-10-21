# Repo Health Inventory

A small, **read-only** Python repository maintenance inventory for maintainers and coding-agent workflows. Checks for a README, explicit licensing, CI workflow, basic test-file presence, and optional packaging, contributing and security files.

**Status:** experimental public source repository at [Csq57/repo-health-check](https://github.com/Csq57/repo-health-check), without a tagged release or independent adoption evidence. It is **not an OpenAI-endorsed tool or proof of eligibility for any subscription programme**.

## Requirements

- Python 3.11 or newer
- No third-party Python runtime dependencies

## Quick start

Clone or unzip this repository, then run from its root:

```shell
python tools/repo_health_check.py .
python tools/repo_health_check.py /path/to/another/repository --format json
python tools/repo_health_check.py /path/to/another/repository --fail-on warning
```

Windows PowerShell works with the same commands using an installed Python launcher, for example `py -3 tools/repo_health_check.py .`.

`--format json` prints a structured inventory for piping to other local tools. `--fail-on warning` turns missing required checks or incomplete scans into a nonzero exit code. Without that flag the tool reports warning conditions but exits successfully for readable roots.

Run its own tests with:

```shell
python -m unittest discover -s tests -p 'test_repo_health_check.py' -v
```

## Checks and status meanings

| Item | Interpretation when missing |
|---|---|
| README | Warning |
| Explicit licence file | Warning |
| GitHub Actions workflow YAML | Warning |
| Python test module | Warning, or explicitly incomplete if the scan did not finish |
| Python packaging metadata | Informational (standalone scripts need not be packages) |
| Contributing guide | Informational |
| Security policy | Informational |

**Exit codes:** `0` for a valid scan in normal mode; `1` in strict mode when any warnings are reported; `2` when the requested root directory is invalid or inaccessible. The tool does not execute the target project's code.

**Scanning limits:** Test discovery skips common generated and virtual-environment folders, does not follow directory symlinks and stops after 20,000 files or 5,000 directories. Filesystem read errors and exceeded limits produce an **incomplete** result rather than a false absence claim. Discovery confirms names, not runnable tests or test coverage.

## Security and privacy boundaries

- Scans only the local directory **you supply**; it does not connect to GitHub or a brokerage and does not request credentials.
- Reads file metadata and directory entries; never reads target source-file contents, imports target modules or executes target tests.
- The JSON output contains an **absolute local path** (`root`). Remove it before sharing logs that may expose personal home-directory names.
- Do not scan directories you are not authorised to inspect, including private repositories and network mounts.
- **Not a malware, legal-compliance or vulnerability scanner.** Finding a LICENSE or CI YAML file does not prove its terms or that the workflow runs correctly.

## Licensing

This **standalone copy** consists of newly authored tool material, licensed under the [MIT License](LICENSE). It intentionally excludes all case-study text, diagrams, samples, financial data and source code from the private OpenTrendIQ-Lite project. The upstream GitHub Actions referenced in CI are external dependencies, not vendored source. See [provenance and third-party notes](docs/PROVENANCE.md).

## Maintainer process

See [CONTRIBUTING.md](CONTRIBUTING.md) to propose improvements and [SECURITY.md](SECURITY.md) for reporting vulnerabilities responsibly. Use the public [issue tracker](https://github.com/Csq57/repo-health-check/issues) for non-sensitive bugs. **Do not include credentials or confidential data.** Private vulnerability reporting has not yet been confirmed enabled; follow [SECURITY.md](SECURITY.md).
