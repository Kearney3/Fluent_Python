"""引发异常而不是返回None"""

def sum(first_number, second_number):
    if isinstance(first_number, int) and isinstance(second_number, int):
        return first_number + second_number
    else:
        raise TypeError('first_number and second_number must be int')

print(sum(1, 2))
print(sum(1, '2'))