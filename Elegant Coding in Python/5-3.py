"""装饰器"""
def to_uppercase(func):
    text = func()

    if not isinstance(text, str):
        raise TypeError("Only strings can be uppercased")
    return text.upper()

def say():
    return "hello"

def hello():
    return "Hello world"

print(to_uppercase(say))
print(to_uppercase(hello))

@to_uppercase
def say():
    return "hello"

print(say)
