"""使用zip"""

user_name = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred']
user_salary = [100, 200, 300, 400, 500, 600]

user = {}
for name, salary in zip(user_name, user_salary):
    user[name] = salary

print(user)