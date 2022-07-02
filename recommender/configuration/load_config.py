"""
This module contain functions to load the configuration file
"""
import sys
import logging
from typing import Any, Dict
import rapidjson
from pathlib import Path
import re

logger = logging.getLogger(__name__)
from exceptions import OperationalException

CONFIG_PARSE_MODE = rapidjson.PM_COMMENTS | rapidjson.PM_TRAILING_COMMAS


def get_config_from_delimited_file(path, delimiter="="):
    config = {}
    with open(path, 'r') as f:
        config_string = f.read()
        lines = config_string.split("\n")
        for line in lines:
            if delimiter in lines:
                key_value = line.split()
                config[key_value[0]] = key_value[1]
    return config


def get_config_from_json_file(path):
    with open(path) if path != '-' else sys.stdin as file:
        config = rapidjson.load(file, parse_mode=CONFIG_PARSE_MODE)
    return config

def log_config_error_range(path: str, errmsg: str) -> str:
    """
    Parses configuration file and prints range around error
    """
    if path != '-':
        offsetlist = re.findall(r'(?<=Parse\serror\sat\soffset\s)\d+', errmsg)
        if offsetlist:
            offset = int(offsetlist[0])
            text = Path(path).read_text()
            # Fetch an offset of 80 characters around the error line
            subtext = text[offset - min(80, offset):offset + 80]
            segments = subtext.split('\n')
            if len(segments) > 3:
                # Remove first and last lines, to avoid odd truncations
                return '\n'.join(segments[1:-1])
            else:
                return subtext
    return ''

def load_config_file(path: str) -> Dict[str, Any]:
    """
    Loads a config file from the given path
    :param path:
    :return:
    """
    try:
        # Read config from json
        if path.endswith(".json"):
            get_config_from_json_file(path)
        # Read config from files delimited with ("=")
        else:
            config = get_config_from_delimited_file(path)
    except FileNotFoundError:
        raise OperationalException(
            f'Config file "{path}" not found!'
            ' Please create a config file or check whether it exists.')
    except rapidjson.JSONDecodeError as e:
        err_range = log_config_error_range(path, str(e))
        raise OperationalException(
            f'{e}\n'
            f'Please verify the following segment of your configuration:\n{err_range}'
            if err_range else 'Please verify your configuration file for syntax errors.'
        )

    return config



