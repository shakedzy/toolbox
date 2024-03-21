# toolbox
A bunch of utilities in Python I find made for myself and found to be generally useful across different projects.

This is not a standalone package, use each file as you wish.


## Available tools

### Dynaconf-based singleton settings class
This Dynaconf-based singleton settings class can be read (and write to) using the same Dynaconf syntax and approach:

Settings file:
```toml
[server]
port = 8888
```
Initialize:
```python
from settings import init_settings

init_settings("path/to/config_files")
```

Usage:
```python
from settings import Settings

port = Settings().server.port
```

### Logger with color support
Usage:
```python
from color_logger import get_logger

logger = get_logger()
logger.error("This is an error!", color="red")
```

Supported colors: red, green, yellow, blue, magenta, cyan

### Time-it decorator

Usage:
```python
from decorators import time_it

@time_it
def function_to_eval():
    pass
```
By default, running duration is printed to debug log.