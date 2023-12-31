from pprint import pprint
from datetime import datetime, timedelta

from ics import Calendar, Event

from huflit_api import PortalPage, User


EMAIL = ""
PASSWORD = ""


def combine_datetime(day: datetime, time: str):
    stime = datetime.strptime(time, "%H:%M").time()
    return datetime.combine(day, stime) + timedelta(
        hours=-7,  # -7 = UTC+7
    )


user = User(EMAIL, PASSWORD)
portal = PortalPage(user)

portal.login_mcs()

semester = portal.get_current_semester()
pprint(semester)

# "Tuesday": [
#     {
#         "lhp": "111111111111",
#         "subject": "Lập trình trên thiết bị di động",
#         "credits": "4",
#         "class_id": "T22101",
#         "time": "9:30 - 12:00",
#         "room": "PM04",
#         "teacher": "Teacher1",
#         "week_study": "(01/01/1990->01/01/1990)",
#     },
# ]

# ------------------------------- #
ical = Calendar()
for day, events in semester.items():
    for event in events:
        split_time = event["time"].split(" - ")
        split_date = event["week_study"].removeprefix("(").removesuffix(")").split("->")

        _date_start = datetime.strptime(split_date[0], "%d/%m/%Y")
        _date_end = datetime.strptime(split_date[1], "%d/%m/%Y")

        while _date_start < _date_end:
            ical_event = Event()
            # parse name
            ical_event.name = f"[{event['room']}] {event['subject']}"
            ical_event.begin = combine_datetime(_date_start, split_time[0].strip())
            ical_event.end = combine_datetime(_date_start, split_time[1].strip())
            ical.events.add(ical_event)
            #
            _date_start += timedelta(days=7)

with open("my.ics", "w", encoding="utf-8") as f:
    f.write(ical.serialize())
