'''列表推导'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# wrong
# squares = list(map(lambda x:x**2, numbers))

# right
squares = [x ** 2 for x in numbers]

print(squares)

data = [1, 'A', 0, False, True]
filter_data = filter(None, data)
for x in filter_data:
    print(x)

filter_data = [item for item in data if item]
print(filter_data)

list_char = ['a', 'b', 'c', 'd', 'e']
vowels = ['a', 'e', 'i', 'o', 'u']
only_vowels = [char for char in list_char if char in vowels]
print(only_vowels)