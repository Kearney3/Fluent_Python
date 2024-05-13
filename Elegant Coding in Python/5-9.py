"""向装饰器传递参数"""

def to_uppercase(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        if not isinstance(text, str):
            raise TypeError("Argument must be a string")
        return text.upper()
    return wrapper

@to_uppercase
def say(greet):
    return greet

print(say("hello there"))
