import typing as typ
import functools as fct
import time

def retry(retries: int = 3, delay: float = 1) -> typ.Callable:
    """
    Attempt to call a function, if it fails, try again with a specified delay.

    :param retries: The max amount of retries you want for the function call
    :param delay: The delay (in seconds) between each function retry
    :return:
    """

    # Don't let the user use this decorator if they are high
    if retries < 1 or delay <= 0:
        raise ValueError('retries or delay cannot be less than zero!!!')

    def decorator(func: typ.Callable) -> typ.Callable:
        @fct.wraps(func)
        def wrapper(*args, **kwargs) -> typ.Any:
            for i in range(1, retries + 1):  # 1 to retries + 1 since upper bound is exclusive

                try:
                    print(f'Running ({i}): {func.__name__}()')
                    return func(*args, **kwargs)
                except Exception as e:
                    # Break out of the loop if the max amount of retries is exceeded
                    if i == retries:
                        print(f'Error: {repr(e)}.')
                        print(f'"{func.__name__}()" failed after {retries} retries.')
                        break
                    else:
                        print(f'Error: {repr(e)} -> Retrying...')
                        time.sleep(delay)  # Add a delay before running the next iteration
        return wrapper

    return decorator

def timer(func: typ.Callable) -> typ.Callable:
    def wrapper(*args, **kwargs) -> typ.Any:
        t1 = time.time()
        func(*args, **kwargs)
        print(f'{func.__name__} took {time.time()-t1} secs. !')
    return wrapper