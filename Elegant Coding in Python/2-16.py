"""使用字典"""

from collections import Counter
from icecream import ic
countries = ['France', 'Germany', 'America', 'Spain', 'America', 'Sweden', 'Switzerland', 'France', 'France']
ic(Counter(countries))
ic(Counter(countries).most_common(1))

