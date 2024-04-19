"""字典排序"""

users = [
    {'name': 'Harry', 'age': 20},
    {'name': 'Ron', 'age': 18},
    {'name': 'Hermione', 'age': 19},
    {'name': 'Draco', 'age': 17},
    {'firsnametname': 'Ginny', 'age': 20},
]


# wrong way
# 无法解决关键字丢失或者字典是否合法的问题
# users = sorted(users, key=lambda user: user['name'].lower())

# Right way
def get_user_name(users):
    """Get name of the user in lower case"""
    return users['name'].lower()


def get_sorted_dict(users):
    """Sort the nested dictionaries"""
    if not isinstance(users, dict):
        raise ValueError("Not a dictionary")
    if not len(users):
        raise ValueError("Empty dictionary")

    users_by_name = sorted(users, key=get_user_name)
    return users_by_name


users_by_name = get_sorted_dict(users)


# Wrong
type(users)

#Right
if isinstance(users, dict):
    pass

