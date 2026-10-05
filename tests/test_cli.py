import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECRET = "SENTINEL_DO_NOT_LEAK_74d0"


class CliTests(unittest.TestCase):
    def run_cli(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        return subprocess.run(
            [sys.executable, "-m", "fintech_research_agents", *arguments],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_help_and_version_need_no_configuration(self):
        for args, expected in ((["--help"], "usage:"), (["--version"], "0.1.0")):
            result = self.run_cli(*args)
            self.assertEqual(result.returncode, 0)
            self.assertIn(expected, result.stdout)
            self.assertEqual(result.stderr, "")

    def test_valid_and_invalid_configs(self):
        with tempfile.TemporaryDirectory() as directory:
            good = Path(directory) / "good.toml"
            bad = Path(directory) / "bad.toml"
            malformed = Path(directory) / "malformed.toml"
            good.write_text('schema_version = 1\nmode = "demo"\n', encoding="utf-8")
            bad.write_text(f'schema_version = 1\nmode = "demo"\n{SECRET} = "x"\n', encoding="utf-8")
            malformed.write_text(f'{SECRET} = "unterminated', encoding="utf-8")
            valid_result = self.run_cli("validate-config", str(good))
            self.assertEqual((valid_result.returncode, valid_result.stdout, valid_result.stderr),
                             (0, "Configuration valid.\n", ""))
            for path in (bad, malformed):
                with self.subTest(path=path.name):
                    result = self.run_cli("validate-config", str(path))
                    self.assertEqual(result.returncode, 2)
                    self.assertNotIn(SECRET, result.stdout + result.stderr)

    def test_unexpected_argument_is_sanitised(self):
        cases = (
            ("unknown command", (SECRET,)),
            ("unexpected top-level option", (f"--{SECRET}",)),
            ("unexpected validate-config option", ("validate-config", f"--{SECRET}")),
        )
        for label, arguments in cases:
            with self.subTest(case=label):
                result = self.run_cli(*arguments)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn(SECRET, result.stdout + result.stderr)

    def test_validation_creates_no_research_or_database_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "good.toml"
            config.write_text('schema_version = 1\nmode = "demo"\n', encoding="utf-8")
            before = {str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file()}
            result = self.run_cli("validate-config", str(config))
            after = {str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file()}
        self.assertEqual(result.returncode, 0)
        self.assertEqual(after, before)


if __name__ == "__main__":
    unittest.main()
