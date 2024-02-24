log= {}
import datetime as dt
def create_function_log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log[func.__name__+'-'+str(dt.datetime.utcnow())] = f'Running {func.__name__} ==> returned {result}'
        return result
    return wrapper

@create_function_log
def add(x, y):
    return x + y
print(add(5,7))
print(add(50, 7))
print(log)