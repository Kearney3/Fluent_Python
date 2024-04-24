"""日志模块"""

import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()

handler.setLevel(logging.DEBUG)
format_c = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(format_c)
logger.addHandler(handler)


def devision(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        logger.exception('devision by zero')


num = devision(1, 2)
num = devision(1, 0)
