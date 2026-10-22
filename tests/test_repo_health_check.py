# SPDX-FileCopyrightText: 2026 Songquan Chen
# SPDX-License-Identifier: MIT
"""Read-only CLI regression tests; Python standard library only."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from tools.repo_health_check import (  # noqa: E402
    MAX_DIRS_TO_INSPECT,
    inspect_repository,
)

SCRIPT = PROJECT_ROOT / 'tools' / 'repo_health_check.py'


class HealthCheckTests(unittest.TestCase):
    @staticmethod
    def statuses(repo: Path) -> dict[str, str]:
        return {check.name: check.status for check in inspect_repository(repo)}

    def test_empty_repository_reports_missing_maintenance_basics(self):
        with tempfile.TemporaryDirectory() as directory:
            status = self.statuses(Path(directory))
            self.assertEqual(status['README'], 'warning')
            self.assertEqual(status['License'], 'warning')
            self.assertEqual(status['Python packaging'], 'info')
            self.assertEqual(status['CI workflow'], 'warning')
            self.assertEqual(status['Tests'], 'warning')
            self.assertEqual(status['Contributing guide'], 'info')

    def test_complete_fixture_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            for relative in (
                'README.md', 'LICENSE', 'pyproject.toml',
                '.github/workflows/test.yml', 'tests/test_feature.py',
                'CONTRIBUTING.md', 'SECURITY.md',
            ):
                path = repo / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('example\n', encoding='utf-8')
            self.assertTrue(all(v == 'pass' for v in self.statuses(repo).values()))

    def test_ignored_virtual_environment_does_not_count_as_tests(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            path = repo / '.venv' / 'tests' / 'test_dependency.py'
            path.parent.mkdir(parents=True)
            path.write_text('not project tests\n', encoding='utf-8')
            self.assertEqual(self.statuses(repo)['Tests'], 'warning')

    def test_symlinked_workflow_is_not_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            external = repo / 'external.yml'
            external.write_text('example\n', encoding='utf-8')
            workflows = repo / '.github' / 'workflows'
            workflows.mkdir(parents=True)
            try:
                (workflows / 'check.yml').symlink_to(external)
            except (OSError, NotImplementedError):
                self.skipTest('Symlinks unavailable in this environment')
            self.assertEqual(self.statuses(repo)['CI workflow'], 'warning')

    def test_json_is_machine_readable_and_nonmutating(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            (repo / 'README.md').write_text('Hello\n', encoding='utf-8')
            before = sorted(str(p.relative_to(repo)) for p in repo.rglob('*'))
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), str(repo), '--format', 'json'],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            parsed = json.loads(completed.stdout)
            self.assertEqual(parsed['warning_count'], 3)
            self.assertEqual(parsed['root'], str(repo.resolve()))
            self.assertEqual(parsed['checks'][0]['name'], 'README')
            self.assertEqual(before, sorted(str(p.relative_to(repo)) for p in repo.rglob('*')))


    def test_redact_root_json_omits_path_and_preserves_checks(self):
        with tempfile.TemporaryDirectory(prefix='oss-private-path-') as directory:
            repo = Path(directory)
            (repo / 'README.md').write_text('example\n', encoding='utf-8')
            result = subprocess.run(
                [sys.executable, str(SCRIPT), directory, '--format', 'json', '--redact-root'],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotIn(directory, result.stdout)
            self.assertNotIn(directory, result.stderr)
            data = json.loads(result.stdout)
            self.assertIsNone(data['root'])
            self.assertEqual(data['warning_count'], 3)
            self.assertEqual(data['checks'][0]['status'], 'pass')

    def test_redact_root_text_hides_path_without_changing_exit_gate(self):
        with tempfile.TemporaryDirectory(prefix='oss-private-path-') as directory:
            result = subprocess.run(
                [sys.executable, str(SCRIPT), directory, '--redact-root',
                 '--fail-on', 'warning'],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertIn('Repository health inventory: [redacted]', result.stdout)
            self.assertNotIn(directory, result.stdout)
            self.assertNotIn(directory, result.stderr)

    def test_redact_root_invalid_path_error_does_not_leak_path(self):
        with tempfile.TemporaryDirectory(prefix='oss-private-path-') as directory:
            missing = str(Path(directory) / 'private-subdir')
            result = subprocess.run(
                [sys.executable, str(SCRIPT), missing, '--redact-root'],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertNotIn(directory, result.stderr)
            self.assertIn('Cannot inspect the supplied directory', result.stderr)

    def test_scan_error_reports_incomplete_search(self):
        with tempfile.TemporaryDirectory() as directory:
            def denied_walk(_root, *, topdown, followlinks, onerror):
                self.assertTrue(topdown)
                self.assertFalse(followlinks)
                onerror(PermissionError('simulated denied directory'))
                return iter(())

            with patch('tools.repo_health_check.os.walk', side_effect=denied_walk):
                test_check = next(
                    c for c in inspect_repository(Path(directory)) if c.name == 'Tests'
                )
            self.assertEqual(test_check.status, 'warning')
            self.assertIn('Incomplete search:', test_check.evidence)
            self.assertIn('directory read error', test_check.evidence)
            self.assertNotIn('No Python test module found', test_check.evidence)

    def test_scan_limit_on_many_empty_directories_is_inconclusive(self):
        with tempfile.TemporaryDirectory() as directory:
            def many_empty_dirs(_root, *, topdown, followlinks, onerror):
                self.assertTrue(topdown)
                self.assertFalse(followlinks)
                self.assertTrue(callable(onerror))
                for _ in range(MAX_DIRS_TO_INSPECT + 1):
                    yield directory, [], []

            with patch('tools.repo_health_check.os.walk', side_effect=many_empty_dirs):
                test_check = next(
                    c for c in inspect_repository(Path(directory)) if c.name == 'Tests'
                )
            self.assertEqual(test_check.status, 'warning')
            self.assertIn('Directory scan limit reached', test_check.evidence)
            self.assertIn('recheck', test_check.next_step)

    def test_nonpackaged_script_is_not_automatically_a_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            (repo / 'README.md').write_text('script usage', encoding='utf-8')
            status = self.statuses(repo)
            self.assertEqual(status['Python packaging'], 'info')

    def test_strict_exit_code_and_invalid_path(self):
        with tempfile.TemporaryDirectory() as directory:
            strict = subprocess.run(
                [sys.executable, str(SCRIPT), directory, '--fail-on', 'warning'],
                capture_output=True, text=True,
            )
            self.assertEqual(strict.returncode, 1)
            invalid = subprocess.run(
                [sys.executable, str(SCRIPT), str(Path(directory) / 'missing')],
                capture_output=True, text=True,
            )
            self.assertEqual(invalid.returncode, 2)
            self.assertIn('Not a directory', invalid.stderr)


if __name__ == '__main__':
    unittest.main()
