"""通过__call__实现缓存"""


class Memo(type):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self._cache = {}

    def __call__(self, _id, *args, **kwargs):
        if _id not in self._cache:
            self._cache[_id] = super().__call__(_id, *args, **kwargs)
        else:
            print('Using cached result')
        return self._cache[_id]


class Foo(Memo):
    def __init__(self, _id, *args, **kwargs):
        self._id = _id


def t():
    f1 = Foo(_id='1')
    f2 = Foo(_id='1')
    print(f1 is f2)


t()
