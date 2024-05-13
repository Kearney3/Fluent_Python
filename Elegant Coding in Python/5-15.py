"""装饰器维护状态"""

class Count:
    def __init__(self, func):
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.count} times")
        return self.func(*args, **kwargs)

@Count
def hello():
    print("hello")

hello()
hello()
hello()