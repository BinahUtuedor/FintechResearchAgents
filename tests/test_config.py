import tempfile
import unittest
from pathlib import Path

from fintech_research_agents.config import ConfigError, Settings, load_settings


class ConfigTests(unittest.TestCase):
    def check_config(self, content: bytes) -> Settings:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.toml"
            path.write_bytes(content)
            return load_settings(path)

    def test_valid_config_is_immutable_settings(self):
        settings = self.check_config(b'schema_version = 1\nmode = "demo"\n')
        self.assertEqual(settings, Settings(schema_version=1, mode="demo"))
        with self.assertRaises((AttributeError, TypeError)):
            settings.mode = "live"

    def test_rejects_missing_unknown_wrong_type_and_unsupported_values(self):
        cases = (
            b'mode = "demo"\n',
            b'schema_version = 1\n',
            b'',
            b'schema_version = 1\nmode = "demo"\nprivate_sentinel = "SENTINEL_CONFIG_KEY"\n',
            b'schema_version = true\nmode = "demo"\n',
            b'schema_version = 1.0\nmode = "demo"\n',
            b'schema_version = "1"\nmode = "demo"\n',
            b'schema_version = 2\nmode = "demo"\n',
            b'schema_version = 1\nmode = "live"\n',
            b'schema_version = 1\nmode = true\n',
        )
        for content in cases:
            with self.subTest(content=content):
                with self.assertRaises(ConfigError) as caught:
                    self.check_config(content)
                self.assertNotIn("SENTINEL_CONFIG_KEY", str(caught.exception))

    def test_malformed_and_invalid_utf8_are_sanitised(self):
        for content in (b'private_sentinel = "SENTINEL_MALFORMED', b"\xff"):
            with self.subTest(content=content):
                with self.assertRaises(ConfigError) as caught:
                    self.check_config(content)
                self.assertNotIn("SENTINEL", str(caught.exception))

    def test_missing_file_has_safe_error(self):
        with self.assertRaisesRegex(ConfigError, "cannot read configuration file"):
            load_settings(Path(tempfile.gettempdir()) / "fra-file-that-does-not-exist.toml")


if __name__ == "__main__":
    unittest.main()
