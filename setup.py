import pathlib
from setuptools import setup, find_packages

### Update these values ###
PACKAGE_NAME = ""
AUTHOR = ""
AUTHOR_EMAIL = ""
HOMEPAGE = ""
LICENSE = ""
DESCRIPTION = ""
CLI_COMMAND_NAME = ""
MIN_PYTHON_MINOR = 11
MAX_PYTHON_MINOR = 12
#######

DOWNLOAD_URL = f"https://pypi.org/project/{PACKAGE_NAME}/"

HERE = pathlib.Path(__file__).parent.resolve()
VERSION = (HERE / "VERSION").read_text(encoding="utf8").strip()

LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf8")
LONG_DESC_TYPE = "text/markdown"

requirements = (HERE / "requirements.txt").read_text(encoding="utf8")
INSTALL_REQUIRES = [s.strip() for s in requirements.split("\n")]

CLASSIFIERS = [
    f"Programming Language :: Python :: 3.{str(v)}" for v in range(MIN_PYTHON_MINOR, MAX_PYTHON_MINOR+1)
]
PYTHON_REQUIRES = f">=3.{str(MIN_PYTHON_MINOR)}"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=HOMEPAGE,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    package_data={
        PACKAGE_NAME: ['resources/*'],  
    },
    entry_points={
        'console_scripts': [
            f'{CLI_COMMAND_NAME} = {PACKAGE_NAME}._cli:run'
        ]
    }
)