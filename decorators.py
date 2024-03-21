from time import time
from datetime import timedelta
from typing import Callable
from .color_logger import get_logger


def time_it(func: Callable):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        elapsed_time = timedelta(seconds=end_time-start_time)
        get_logger().debug(f"{func.__name__} run duration: {str(elapsed_time)}")
        return result
    return wrapper
