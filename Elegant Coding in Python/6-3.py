"""可以停止的迭代器"""

class MutiplyByTwo:
    def __init__(self, num, limit):
        self.num = num
        self.limit = limit
        self.count = 0

    def __next__(self):
        self.count += 1
        value = self.num * self.count
        if value > self.limit:
            raise StopIteration
        else:
            return value

    def __iter__(self):
        return self

for num in MutiplyByTwo(5, 500):
    print(num)