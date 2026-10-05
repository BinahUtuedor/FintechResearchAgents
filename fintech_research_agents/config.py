"""Strict loading and validation for the minimal demo configuration."""

from dataclasses import dataclass
from pathlib import Path
import tomllib


@dataclass(frozen=True)
class Settings:
    schema_version: int
    mode: str


class ConfigError(ValueError):
    """A sanitised configuration error safe to show to a CLI user."""


def load_settings(path: str | Path) -> Settings:
    """Load the exact supported TOML settings, without exposing file data."""
    try:
        with Path(path).open("rb") as config_file:
            data = tomllib.load(config_file)
    except OSError:
        raise ConfigError("cannot read configuration file") from None
    except tomllib.TOMLDecodeError:
        raise ConfigError("malformed TOML configuration") from None
    except UnicodeError:
        raise ConfigError("configuration is not valid UTF-8") from None

    if not isinstance(data, dict):
        raise ConfigError("configuration must be a TOML table")

    expected = {"schema_version", "mode"}
    if set(data) != expected:
        if "schema_version" not in data or "mode" not in data:
            raise ConfigError("configuration requires schema_version and mode")
        raise ConfigError("configuration contains unsupported fields")

    version = data["schema_version"]
    if type(version) is not int:
        raise ConfigError("schema_version must be integer 1")
    if version != 1:
        raise ConfigError("unsupported schema_version")
    if not isinstance(data["mode"], str):
        raise ConfigError("mode must be the string demo")
    if data["mode"] != "demo":
        raise ConfigError("unsupported mode")

    return Settings(schema_version=1, mode="demo")
