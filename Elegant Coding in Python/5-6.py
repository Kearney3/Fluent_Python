"""大小写装饰器"""

def to_uppercase(func):
    def wrapper():
        text = func()
        if not isinstance(text, str):
            raise TypeError("The decorated function must return a string")
        return text.upper()
    return wrapper

@to_uppercase
def hello_world():
    return "hello world"

print(hello_world())