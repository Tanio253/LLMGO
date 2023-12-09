import time
from functools import wraps

def retry_with_delay(max_retries=5, delay=60):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < max_retries:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        raise
        return wrapper
    return decorator
