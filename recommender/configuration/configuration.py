import logging
from copy import deepcopy
from typing import Any, Dict, List, Optional
from constants import CONFIG_OPTION_NAME, MINIMAL_CONFIG
from load_config import load_config_file
from misc import deep_merge_dicts

logger = logging.getLogger(__name__)


class Configuration:

    def __init__(self, args: Dict[str, Any]) -> None:
        self.args = args
        self.config: Optional[Dict[str, Any]] = None

    def get_config(self) -> Dict[str, Any]:
        if self.config is None:
            self.config = self.load_config()

        return self.config

    def load_config(self) -> Dict[str, Any]:
        config: Dict[str, Any] = self.load_from_files(self.args.get(CONFIG_OPTION_NAME))

        # Process of mandatory fields
        self._process_logging_options(config)
        self._process_datasource_details(config)
        self._process_required_folders(config)

        return config

    def load_from_files(self, files: List[str]) -> Dict[str, Any]:

        # Keep this method as staticmethod, so it can be used from interactive environments
        config: Dict[str, Any] = {}

        # We expect here a list of config filenames
        if not files:
            logger.warning(f"Config file(s) not sepcified, using minimal config")
            config = deepcopy(MINIMAL_CONFIG)

        for path in files:
            logger.info(f'Parsing config: {path} .. ')

            # Merge config options, overwriting old values
            config = deep_merge_dicts(load_config_file(path), config)

        return config

    def _process_logging_options(self, config: Dict[str, Any]) -> None:
        """
        Extract information for sys.argv and load logging configuration:
        the -v/--verbose, --logfile options
        """
        # Log level
        config.update({'verbosity': self.args.get('verbosity', 0)})

        if 'logfile' in self.args and self.args['logfile']:
            config.update({'logfile': self.args['logfile']})

        setup_logging(config)
