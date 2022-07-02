from constants import ENV_OPTION_NAME, CONFIG_OPTION_NAME, LOGFILE_OPTION_NAME, VERBOSITY_OPTION_NAME, \
    USER_DIR_OPTION_NAME


class Arg:

    def __init__(self, *args, **kwargs):
        self.cli = args
        self.kwargs = kwargs


AVAILABLE_CLI_OPTIONS = {
    ENV_OPTION_NAME: Arg(
        metavar="ENV",  # Placeholder display name
        help=f'Specify environment '
             f'e.g. DEV/UAT/PROD'
    ),

    CONFIG_OPTION_NAME: Arg(
        '-c', '--config',
        help=f'Specify configuration file'
             f'Multiple --config options may be used.',
        required=False,
        action='append',
        metavar='CONFIG_FILE(S)'
    ),

    LOGFILE_OPTION_NAME: Arg(
        '--logfile',
        help="Log to the file specified. Special values are: 'syslog', 'journald'. "
             "See the documentation for more details.",
        metavar='FILE',
    ),

    VERBOSITY_OPTION_NAME: Arg(
        '-v', '--verbose',
        help='Verbose mode (-vv for more, -vvv to get all messages).',
        action='count',
        default=0,
    ),

    USER_DIR_OPTION_NAME: Arg(
        '--userdir', '--user-data-dir',
        help='Path to userdata directory.',
        metavar='PATH',
    ),
}
