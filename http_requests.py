import requests
from requests import Response
from requests.cookies import RequestsCookieJar
from bs4 import BeautifulSoup


class HttpRequests:
    def __init__(self):
        self.requests: requests.sessions.Session = requests.sessions.Session()

    def _set_cookies(self, cookies: RequestsCookieJar):
        self.cookies = cookies

    def post(self, end_point: str, payload: dict, headers: dict = None, **kwargs) -> Response:
        response = self.requests.post(url=end_point, headers=headers, params=payload, **kwargs)
        if response.status_code != 200:
            raise ValueError("requestに失敗しました")
        print(response.url)
        print(response.headers)

        return response

    def get(self, end_point: str, headers: str = None, **kwargs) -> Response:
        response = self.requests.get(url=end_point, headers=headers, **kwargs)
        if response.status_code != 200:
            raise ValueError("requestに失敗しました")

        return response
