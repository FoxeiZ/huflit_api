from datetime import datetime, date, timedelta

from ics import Calendar, Event

from huflit_api import PortalPage, User
from huflit_api.utils import dayname


EMAIL = ""
PASSWORD = ""


def to_datetime(day: str, time: str):
    today = date.today()
    weekday = today.weekday()

    stime = datetime.strptime(time, "%H:%M").time()
    return datetime.combine(today, stime) + timedelta(
        days=dayname.to_int(day) - weekday,
        hours=-7,  # -7 = UTC+7
    )


user = User(EMAIL, PASSWORD)
portal = PortalPage(user)

portal.login_mcs()


# ------------------------------- #
ical = Calendar()
term = portal.get_current_term()
year = 2023

for week in portal.get_week_list().values():
    schedule = portal.get_week_schedule(year, term, week)
    for day, events in schedule.items():
        for event in events:
            split_time = event["time"].split(" - ")
            ical_event = Event()
            # parse name
            ical_event.name = f"[{event['room']}] {event['subject'].split(' (')[0]}"
            ical_event.begin = to_datetime(day, split_time[0].strip())
            ical_event.end = to_datetime(day, split_time[1].strip())
            ical.events.add(ical_event)

with open("my.ics", "w", encoding="utf-8") as f:
    f.write(ical.serialize())
