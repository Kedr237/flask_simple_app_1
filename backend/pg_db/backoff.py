import time
from functools import wraps

from .logger import logger


def backoff(start_delay=0.1, end_delay=10, factor=2, max_attempts=20):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            delay = start_delay
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error(
                        f'[Error] Error in {func.__name__}: {e}')
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(
                            f'[Error] Exceeded maximum attempts for {func.__name__}')
                        raise
                    if delay < end_delay:
                        delay = min(delay * factor, end_delay)
                    logger.info(
                        f'[Info] Retrying {func.__name__} ({delay} seconds)')
                    time.sleep(delay)
        return inner
    return wrapper
