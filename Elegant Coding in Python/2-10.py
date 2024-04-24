"""使用生成器产生素数"""

from collections import namedtuple
import math

from icecream import ic


def is_prime(n):
    """判断素数"""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(lower, higher):
    """获取指定范围内的素数"""
    for possible_prime in range(lower, higher):
        if is_prime(possible_prime):
            yield possible_prime
        yield False

for prime_number in get_prime_numbers(1, 100):
    if prime_number:
        print(prime_number)
