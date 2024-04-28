"""类的属性装饰器"""

class Temperature:
    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def fahrenheit(self):
        return self._temperature

    @fahrenheit.setter
    def fahrenheit(self, temperature):
        if not isinstance(temperature, (int, float)):
            raise TypeError('Wrong type')
        self._temperature = temperature * 9 / 5 + 32

T1 = Temperature(10)
print(T1.temperature)
T1.fahrenheit = 10
print(T1.fahrenheit)
print(T1.temperature)
