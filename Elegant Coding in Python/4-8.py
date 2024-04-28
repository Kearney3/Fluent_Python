"""验证__new__"""

from abc import abstractmethod, ABCMeta
class UserAbstract(metaclass=ABCMeta):
    # Abstract base class template, implementing factory pattern using __new__() initializer.
    def __new__(cls, *args, **kwargs):
    # Creates an object instance and sets a base property.
        obj = object.__new__(cls)
        given_data = args[0]
        # Validating the data here
        if not isinstance(given_data, str):
            raise ValueError(f"Please provide string: {given_data}")
        return obj


class User(UserAbstract):
# Implement UserAbstract class and add its own variable.
    def __init__(self, name):
        self.name = name


user = User("John")
print(user.name)
user = User(123)