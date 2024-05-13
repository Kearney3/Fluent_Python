"""在类的方法上使用装饰器"""
import time
from functools import wraps

from sphinx.util import requests


def retry_requests(tries=3, delay = 10):
    def try_requests(func):
        @wraps(func)
        def try_decorator(*args, **kwargs):
            for i in range(tries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(e)
                    time.sleep(delay)
        return try_decorator
    return try_requests

class ApiRequest:
    def __init__(self, url):
        self.url = url
    @retry_requests(tries=3, delay=5)
    def make_request(self):
        try:
            response = requests.get(self.url)
            if response.status_code in (500,502,503,429):
                pass
        except:
            pass


