"""同时使用多个装饰器"""

def add_prefix(func):
    def wrapper():
        text = func()
        if not isinstance(text, str):
            raise TypeError("The decorated function must return a string")
        result = '.'.join(['A prefix ', text])
        return result
    return wrapper

def to_uppercase(func):
    def wrapper():
        text = func()
        if not isinstance(text, str):
            raise TypeError("The decorated function must return a string")
        result = text.upper()
        return result
    return wrapper

@add_prefix
@to_uppercase
def say():
    return 'hello world'

@to_uppercase
@add_prefix
def hello():
    return 'hello world'

print(say())
print(hello())