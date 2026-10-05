"""Command line interface for the minimal local scaffold."""

import argparse
from collections.abc import Sequence
import sys

from . import __version__
from .config import ConfigError, load_settings


class _SafeArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        # argparse's default includes the offending token, which may be secret.
        self.print_usage(sys.stderr)
        self.exit(2, f"{self.prog}: invalid command or arguments\n")


def _parser() -> _SafeArgumentParser:
    parser = _SafeArgumentParser(
        prog="python -m fintech_research_agents",
        description="Local FintechResearchAgents configuration utility.",
    )
    parser.add_argument("--version", action="version", version=__version__)
    commands = parser.add_subparsers(dest="command")
    validate = commands.add_parser("validate-config", help="validate a TOML configuration")
    validate.add_argument("path", help="path to the configuration file")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    try:
        load_settings(args.path)
    except ConfigError as error:
        print(f"Configuration invalid: {error}", file=sys.stderr)
        return 2
    print("Configuration valid.")
    return 0
