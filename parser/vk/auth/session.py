import urllib3
from urllib3 import PoolManager
from http.cookiejar import CookieJar
from urllib3.util import parse_url


class HTTP:
    http = PoolManager()
    cookie_jar = CookieJar()
    http.cookie_jar = cookie_jar


class Opener(HTTP):
    @classmethod
    def open(cls, url: str) -> str:
        response = cls.http.request(
            method='GET',
            url=url
        )
        return response
