from argparse import ArgumentParser
from . import __version__
from .utils import path_to_resource
from .color_logger import set_default_level
from .settings import init_settings


def _validate_log_level(level: str) -> bool:
    return level.upper() in ['DEBUG', 'INFO', 'WARN', 'WARNING', 'ERROR', 'CRITICAL']


def run(args=None):
    parser = ArgumentParser(description="")
    parser.add_argument('-l', '--log-level', default='INFO', dest='log', help='Set default logging level', type=str)
    parser.add_argument('--version', help='Show version', dest='show_version', default=False, action='store_true')
    parser.add_argument('--config-path', help='Show path to config file', dest='config_path', default=False, action='store_true')
    args = parser.parse_args()

    if not _validate_log_level(args.log):
        raise ValueError(f'Invalid log level {args.log}')

    if args.show_version:
        print(f"Running version: {__version__}")
    elif args.config_path:
        config_path = path_to_resource('config.toml')
        print(f"Config file path: {config_path}")
    else:
        set_default_level(args.log)
        config_path = path_to_resource('config.toml')
        init_settings([config_path])
        # run app
        