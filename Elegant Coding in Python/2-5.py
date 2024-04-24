"""namedtuple实现"""

from collections import namedtuple
from icecream import ic

Point = namedtuple('Point', ['x', 'y', 'z'])
point = Point(x=1, y=2, z=3)
ic(point.x)
ic(point.y)
ic(point.z)


def get_user_info(user_obj):
    user = get_data_from_db(user_obj)
    UserInfo = namedtuple('UserInfo', ['first_name', 'last_name', 'age', 'address'])
    user_info = UserInfo(first_name=user['first_name'], last_name=user['last_name'], age=user['age'], address=user[
        'address'])
    return user_info


def get_full_name(user_info)
    return user_info.first_name + ' ' + user_info.last_name
