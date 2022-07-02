import argparse
from typing import Any, Dict, List, Optional
import logging
from commands.cli_options import AVAILABLE_CLI_OPTIONS
from constants import ENV_OPTION_NAME, CONFIG_OPTION_NAME
logger = logging.getLogger(__name__)

ARGS_LIST = [ENV_OPTION_NAME, CONFIG_OPTION_NAME]


class Arguments:
    """
    Arguments class. Manage the arguments received by the cli
    """

    def __init__(self, args: Optional[List[str]]) -> None:
        self.args = args
        self._parser = None
        self._parsed_args: Optional[argparse.Namespace] = None

    def get_parsed_arg(self) -> Dict[str, Any]:
        """
        :return: List[str] List of arguments
        """

        if self._parsed_args is None:
            self._build_subcommands()  # Build argparser
            self._parsed_args = self._parsed_args()  # parse args

        return vars(self._parsed_args)

    def _build_subcommands(self) -> None:
        self._parser = argparse.ArgumentParser(add_help=False)
        self._build_args(option_list=ARGS_LIST, parser=self._parser)

    def _build_args(self, option_list, parser):
        for option in option_list:
            opt = AVAILABLE_CLI_OPTIONS[option]
            logger.info(f"{option} {opt.cli} {opt.kwargs}")
            parser.add_argument(*opt.cli, dest=option, **opt.kwargs)

    def _parse_args(self) -> argparse.Namespace:
        """
        Parse given arguments and return an argparse Namespace instance
        :return:
        """
        parsed_arg = self._parser.parse_args(self.args)
        return parsed_arg
