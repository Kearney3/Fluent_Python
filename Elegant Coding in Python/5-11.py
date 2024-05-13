"""使用functools库创建装饰器"""
from functools import wraps

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling {}".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@logging
def foo(x):
    return x * x

if __name__ == "__main__":
    print(foo(2))

