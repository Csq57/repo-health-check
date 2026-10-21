# Code provenance and third-party boundaries

## Exact source of extracted files

Source project: `Csq57/ai-python-repository-stabilization-case-study`, public draft [PR #1](https://github.com/Csq57/ai-python-repository-stabilization-case-study/pull/1), verified at commit `9e2f1caab9da012854b44db0d434e326b88d08e1` on 21 October 2026.

The following three files were copied byte-for-byte, verified against the original Git blob hashes via `git hash-object`:

| Standalone file | Git blob SHA-1 in source PR |
|---|---|
| `tools/repo_health_check.py` | `ee24048c17fdd884cb8c95cef728efc61f270d0f` |
| `tests/test_repo_health_check.py` | `f4a988bc90cd12e53692a39df646e8c82ce0a9d0` |
| `.github/workflows/repo-health-check.yml` | `2038264339eae23bb9377fe68befa62607901102` |

The root `LICENSE` is the same bytes as `tools/LICENSE` in the source PR (Git blob `bf660e8ce916667307c8f7b08dbf05e789d72993`). The new README, security, contributing and supporting notes were written specifically for the extracted standalone repository.

## Not copied

No case-study illustrations, `CASE_STUDY.md` or historic materials, client data, private OpenTrendIQ-Lite source, financial/account information or PR Git history were copied. Creating a fresh repository with a fresh first commit avoids *copying* historical commit emails to the new project, but cannot erase the old public PR history.

## External actions (CI only)

CI refers to GitHub's own `actions/checkout` and `actions/setup-python` using their pinned upstream commit IDs. Upstream projects publish their own MIT licences; no GitHub Action source code is included. Review the official upstream projects and update pinned hashes under code review when appropriate. Avoid pasting arbitrary CI secrets or using elevated write scopes.

## Assurance limits

This is an engineering provenance review, not a legal opinion or a comprehensive malware, vulnerability or credentials audit. Verify the rights-holder's identity, any future contributions, and release metadata before publication.
