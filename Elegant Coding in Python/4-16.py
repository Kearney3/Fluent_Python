"""__get__实例"""

import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def __get__(self, instance, owner):
        return random.randint(1, self.sides)

    def __set__(self, instance, value):
        print(f'New assignment: {value}')
        if not isinstance(value, int):
            raise TypeError('Only integers are allowed')
        self.sides = value


class Play:
    d6 = Dice()
    d10 = Dice(10)
    d20 = Dice(20)

play = Play()
print(play.d6)
print(play.d10)
print(play.d20)
play.d6=11
for i in range(10):
    print(play.d6)