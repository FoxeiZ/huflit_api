from bs4 import BeautifulSoup
import httpx


__all__ = ["BasePage"]


class BasePage:
    BASE_URL: str
    session: httpx.Client

    def _do_request(self, method: str, endpoint: str, *args, **kwargs):
        session = getattr(self, "session", httpx.Client())
        r = session.request(
            method, self.BASE_URL + endpoint, follow_redirects=True, *args, **kwargs
        )
        r.raise_for_status()

        session.cookies.update(r.cookies)
        return r

    def request_to_soup(self, method: str, endpoint: str, *args, **kwargs):
        r = self._do_request(method, endpoint, *args, **kwargs)
        return BeautifulSoup(r.text, "html.parser")
