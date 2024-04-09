import pkg_resources
from . import __package_name__


def path_to_resource(filename: str) -> str:
    return pkg_resources.resource_filename(__package_name__, f'resources/{filename}')
