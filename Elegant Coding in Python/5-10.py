"""日志记录装饰器"""

def logging(func):
    def logs(*args, **kwargs):
        print("{0} was called".format(func.__name__))
        return func(*args, **kwargs)
    return logs

@logging
def foo(x):
    return x * x

if __name__ == "__main__":
    print(foo(2))