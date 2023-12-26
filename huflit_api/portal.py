import json
import httpx
from .utils.cache import lru_cache, timed_lru_cache
from datetime import date

from bs4 import BeautifulSoup

from .base import BasePage
from .user import User
from .utils import dayname, period_time

from .constants import portal as CONSTANTS_PORTAL
from .constants import mcs as CONSTANTS_MCS

from .errors import WrongCredentials


__all__ = ["PortalParser", "PortalPage"]


class PortalParser:
    @staticmethod
    def parse_notification(html: str):
        parsed_data: list[dict[str, str]] = []
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find(
            "table", {"class": "table table-bordered table-striped table-responsive"}
        )

        for idx, tr in enumerate(table.find_all("tr")):  # type: ignore
            if idx == 0:
                continue

            td = tr.find_all("td")
            parsed_data.append(
                {"title": td[0].text, "author": td[1].text, "time_sent": td[2].text}
            )
        return parsed_data

    @staticmethod
    def parse_schedule(html: str):
        parsed_data: dict[str, list[dict[str, str]]] = dict()
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table", {"class": "table MainTb"})
        all_periods = table.find_all("div")  # type: ignore
        for period in all_periods:
            day_name = dayname.from_str(period.get("title"))
            if not parsed_data.get(day_name):
                parsed_data[day_name] = []

            data = list(period._all_strings(True))
            parsed_data[day_name].append(
                {
                    "room": data[0],
                    "subject": data[1],
                    "lhp": data[2][5:],
                    "periods": data[3][9:],
                    "period_detail": data[4][6:],
                    "time": " - ".join(period_time.from_detail_periods(data[4][6:])),
                    "teacher": data[5][4:],
                }
            )

        return parsed_data

    @staticmethod
    def parse_semester(html: str):
        parsed_data: dict[str, str] = dict()
        soup = BeautifulSoup(html, "html.parser")


class PortalPage(BasePage):
    BASE_URL = "https://portal.huflit.edu.vn"

    def __init__(self, user: User, **kwargs) -> None:
        self.user: User = user
        self.session = httpx.Client()

        self.is_login = False

        self.session.get(PortalPage.BASE_URL)

    def login_mcs(self):
        """
        Login to portal using Microsoft authentication.

        This is a pain in the ass to write so it better works.
        """
        if self.is_login:
            return

        login_soup = self.request_to_soup(
            "GET",
            CONSTANTS_PORTAL.LOGIN_PAGE_MCS_URL,
        )

        login_raw_data = login_soup.find("script").text  # type: ignore
        login_data = json.loads(login_raw_data[20:-7])
        login_payload = {
            "i13": "0",
            "login": self.user.email,
            "loginfmt": self.user.email,
            "type": "11",
            "LoginOptions": "3",
            "lrt": "",
            "lrtPartition": "",
            "hisRegion": "",
            "hisScaleUnit": "",
            "passwd": self.user.password,
            "ps": "2",
            "psRNGCDefaultType": "",
            "psRNGCEntropy": "",
            "psRNGCSLK": "",
            "canary": login_data["canary"],
            "ctx": login_data["sCtx"],
            "hpgrequestid": login_data["sessionId"],
            "flowToken": login_data["sFT"],
            "PPSX": "",
            "NewUser": "1",
            "FoundMSAs": "",
            "fspost": "0",
            "i21": "0",
            "CookieDisclosure": "0",
            "IsFidoSupported": "1",
            "isSignupPost": "0",
            "i19": "362804",
        }

        post_req = self.session.request(
            "POST",
            CONSTANTS_MCS.BASE_URL + login_data["urlPost"],
            data=login_payload,
            follow_redirects=True,
        )
        post_soup = BeautifulSoup(post_req.text, "html.parser")
        post_data = json.loads(post_soup.find("script").text[20:-7])  # type: ignore

        kmsi_payload = {
            "LoginOptions": "3",
            "type": "28",
            "ctx": post_data["sCtx"],
            "hpgrequestid": post_data["sessionId"],
            "flowToken": post_data["sFT"],
            "canary": post_data["canary"],
            "i19": "1824",
        }
        kmsi_req = self.session.request(
            "POST",
            CONSTANTS_MCS.KMSI,
            data=kmsi_payload,
            follow_redirects=True,
        )

        form_soup = BeautifulSoup(kmsi_req.text, "html.parser").find("form")
        form_data: dict[str, str] = {}
        for input_form in form_soup.find_all("input"):  # type: ignore
            if input_form.has_attr("name"):
                form_data[input_form.get("name")] = input_form.get("value")

        final_req = self._do_request("POST", "/", data=form_data)
        if final_req.status_code == 200:
            self.is_login = True
            return

        raise WrongCredentials("Login failed. Check username and password")

    def login(self) -> None:
        """
        Login to portal.

        Obsolete. Use `login_mcs`. Due to school policy, this method is no longer usable.
        """
        r = self._do_request(
            "POST",
            CONSTANTS_PORTAL.LOGIN_PAGE_URL,
            data={
                CONSTANTS_PORTAL.LOGIN_USER_ARGS: self.user.email,
                CONSTANTS_PORTAL.LOGIN_PASS_ARGS: self.user.password,
            },
        )

        if r.status_code == 200:
            return

        raise WrongCredentials("Login failed. Check username and password")

    def get_notification(self):
        """
        Get the notification of portal.

        Due to bad web design, we somehow need to redirect from MCS login just to access the homepage.
        Then we can get the notification.
        """
        if not self.is_login:
            self.login_mcs()

        home_req = self._do_request("GET", CONSTANTS_PORTAL.HOME_URL)

        form_soup = BeautifulSoup(home_req.text, "html.parser").find("form")
        form_data: dict[str, str] = {}
        for input_form in form_soup.find_all("input"):  # type: ignore
            if input_form.has_attr("name"):
                form_data[input_form.get("name")] = input_form.get("value")

        final_req = self._do_request("POST", "/", data=form_data)
        return PortalParser.parse_notification(final_req.text)

    @timed_lru_cache(maxsize=2)
    def get_current_term(self):
        req = self._do_request("GET", CONSTANTS_PORTAL.SCHEDULE_URL)
        soup = BeautifulSoup(req.text, "html.parser")
        return int(
            soup.find("select", {"id": "TermID"})
            .find("option", {"selected": "selected"})  # type: ignore
            .text[-1]  # type: ignore
        )

    @lru_cache(maxsize=12)
    def get_week_list(self, year: int | None = None, term: int | None = None):
        if not self.is_login:
            self.login_mcs()

        if not year:
            year = date.today().year

        if not term:
            term = self.get_current_term()

        req = self._do_request(
            "GET", f"{CONSTANTS_PORTAL.API_WEEK_URL}/{year}-{year+1}$HK0{term}"
        )
        return {d["DisPlayWeek"]: d["Week"] for d in req.json()}

    @lru_cache(maxsize=12)
    def get_week_schedule(self, year: int, term: int, week: int) -> str:
        """
        Retrieves the weekly schedule for a given year, term, and week.

        Args:
        --------
            year (int): The year of the schedule.
            term (int): The term of the schedule.
            week (int): The week of the schedule.

        Returns:
        --------
            str: The text representation of the weekly schedule.
        """
        if not self.is_login:
            self.login_mcs()

        url = CONSTANTS_PORTAL.DRAWING_SCHEDULE_URL
        params = {
            "YearStudy": f"{year}-{year + 1}",
            "TermID": f"HK0{term}",
            "Week": week,
        }
        response = self._do_request("GET", url, params=params)
        return response.text

    def get_weekly_schedule(self):
        """
        Retrieves the weekly schedule for the current term.
        """
        current_date = date.today().isocalendar()
        current_week = current_date[1]
        current_year = current_date[0]

        data = self.get_week_schedule(
            current_year, self.get_current_term(), current_week
        )
        return PortalParser.parse_schedule(data)

    def get_semester(self):
        current_year = date.today().year
        current_term = self.get_current_term()

        data = self._do_request(
            "GET",
            CONSTANTS_PORTAL.SEMESTER_SCHEDULE_URL,
            params={"YearStudy": current_year, "TermID": f"HK0{current_term}"},
        )

        return PortalParser.parse_semester(data.text)
