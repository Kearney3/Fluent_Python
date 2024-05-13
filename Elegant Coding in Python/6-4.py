"""生成器"""

def multi_generator(num, limit):
    counter = 1
    value = num * counter

    while value < limit:
        yield value
        counter += 1
        value = num * counter

for i in multi_generator(2,50):
    print(i)