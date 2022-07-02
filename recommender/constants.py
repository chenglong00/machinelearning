ENV_OPTION_NAME = "env"
CONFIG_OPTION_NAME = "config"
LOGFILE_OPTION_NAME = "logfile"
VERBOSITY_OPTION_NAME = "verbosity"
USER_DIR_OPTION_NAME = "user_dir"

MINIMAL_CONFIG = {
    'stake_currency': '',
    'dry_run': True,
    'exchange': {
        'name': '',
        'key': '',
        'secret': '',
        'pair_whitelist': [],
        'ccxt_async_config': {
            'enableRateLimit': True,
        }
    }
}
