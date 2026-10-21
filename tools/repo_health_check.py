#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Songquan Chen
# SPDX-License-Identifier: MIT
"""Read-only, zero-dependency checks for a Python repository's basic upkeep.

This is a small inventory, not a test runner, security scan, or OSS certification.
"""
from __future__ import annotations

import argparse
import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

SKIP_DIRS = frozenset({
    '.git', '.venv', 'venv', 'env', 'node_modules', 'site-packages',
    '.tox', '.nox', '.pytest_cache', '.mypy_cache', '__pycache__',
    'build', 'dist', '.ruff_cache', '.idea', '.vscode',
})
MAX_FILES_TO_INSPECT = 20_000
MAX_DIRS_TO_INSPECT = 5_000


@dataclass(frozen=True)
class Check:
    name: str
    status: str  # pass, warning, info
    evidence: str
    next_step: str


def _first_file(root: Path, names: Iterable[str]) -> str | None:
    for name in names:
        candidate = root / name
        if candidate.is_file() and not candidate.is_symlink():
            return name
    return None


def _test_files(root: Path) -> tuple[bool, str | None]:
    """Return (test_found, incomplete_reason); never follow directory symlinks.

    A detected test module is a conclusive presence check. If no test is found,
    filesystem errors or scan limits must be reported as inconclusive.
    """
    files_seen = 0
    dirs_seen = 0
    walk_errors = 0

    def onerror(_error: OSError) -> None:
        nonlocal walk_errors
        walk_errors += 1

    for current, dirs, files in os.walk(
        root, topdown=True, followlinks=False, onerror=onerror
    ):
        dirs_seen += 1
        if dirs_seen > MAX_DIRS_TO_INSPECT:
            return False, f'Directory scan limit reached ({MAX_DIRS_TO_INSPECT})'
        dirs[:] = sorted(
            d for d in dirs
            if d not in SKIP_DIRS and not (Path(current) / d).is_symlink()
        )
        for filename in sorted(files):
            files_seen += 1
            if files_seen > MAX_FILES_TO_INSPECT:
                return False, f'File scan limit reached ({MAX_FILES_TO_INSPECT})'
            file_path = Path(current) / filename
            if file_path.is_symlink() or not file_path.is_file():
                continue
            # Inventory checks file names only; it never imports or runs tests.
            if filename.startswith('test_') and filename.endswith('.py'):
                return True, None
            if filename.endswith('_test.py'):
                return True, None
    if walk_errors:
        return False, f'{walk_errors} directory read error(s)'
    return False, None


def inspect_repository(root: Path) -> list[Check]:
    if not root.is_dir():
        raise ValueError(f'Not a directory: {root}')
    checks: list[Check] = []

    def record(name: str, found: str | None, missing_next: str, *, required: bool = True) -> None:
        checks.append(Check(
            name=name,
            status='pass' if found else ('warning' if required else 'info'),
            evidence=f'Found: {found}' if found else 'Not found',
            next_step='' if found else missing_next,
        ))

    record('README', _first_file(root, ('README.md', 'README.rst', 'README.txt', 'README')),
           'Document purpose, installation and verification commands.')
    record('License', _first_file(root, ('LICENSE', 'LICENSE.md', 'LICENSE.txt', 'COPYING', 'COPYING.md')),
           'Make a deliberate licensing decision with the rights holder; public code is not automatically open source.')
    record('Python packaging', _first_file(root, ('pyproject.toml', 'setup.cfg', 'setup.py')),
           'If distributing a Python package, provide build/install metadata; scripts need not be packages.', required=False)

    workflows = root / '.github' / 'workflows'
    workflow_found = None
    if workflows.is_dir() and not workflows.is_symlink():
        for child in sorted(workflows.iterdir()):
            if child.is_file() and not child.is_symlink() and child.suffix.lower() in ('.yml', '.yaml'):
                workflow_found = str(child.relative_to(root))
                break
    record('CI workflow', workflow_found,
           'Add repeatable checks in CI; a workflow file alone does not prove that CI succeeds.')

    tests_found, incomplete_reason = _test_files(root)
    checks.append(Check(
        name='Tests',
        status='pass' if tests_found else 'warning',
        evidence=(
            'Found a Python test module' if tests_found
            else f'Incomplete search: {incomplete_reason}' if incomplete_reason
            else 'No Python test module found'
        ),
        next_step=(
            '' if tests_found
            else 'Resolve filesystem errors or scan limits, then recheck.'
            if incomplete_reason
            else 'Add regression tests and document how to run them.'
        ),
    ))
    record('Contributing guide', _first_file(root, ('CONTRIBUTING.md', '.github/CONTRIBUTING.md')),
           'Explain how others can report bugs and propose changes.', required=False)
    record('Security policy', _first_file(root, ('SECURITY.md', '.github/SECURITY.md')),
           'Consider private vulnerability-reporting instructions.', required=False)
    return checks


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', default='.', help='Repository directory; default: current directory')
    parser.add_argument('--format', choices=('text', 'json'), default='text')
    parser.add_argument('--fail-on', choices=('none', 'warning'), default='none',
                        help='Exit with status 1 when a warning exists; default does not fail')
    args = parser.parse_args(argv)
    try:
        path = Path(args.path).expanduser().resolve()
        checks = inspect_repository(path)
    except (ValueError, OSError) as exc:
        parser.exit(2, f'repo-health-check: {exc}\n')

    if args.format == 'json':
        print(json.dumps({
            'root': str(path),
            'checks': [asdict(c) for c in checks],
            'warning_count': sum(c.status == 'warning' for c in checks),
            'limits': ['Read-only; no code executed, no network calls, no quality or security certification.'],
        }, indent=2, ensure_ascii=False))
    else:
        print(f'Repository health inventory: {path}')
        for c in checks:
            print(f'[{c.status.upper():7}] {c.name}: {c.evidence}')
            if c.next_step:
                print(f'          Next: {c.next_step}')
        print('Inventory only: does not execute tests, verify CI success, or certify open-source eligibility.')
    if args.fail_on == 'warning' and any(c.status == 'warning' for c in checks):
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
