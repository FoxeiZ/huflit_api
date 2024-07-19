from typing import TypedDict

SemesterDict = TypedDict(
    "SemesterDict",
    {
        "lhp": str,
        "subject": str,
        "credits": str,
        "class_id": str,
        "time": str,
        "period_detail": str,
        "room": str,
        "teacher": str,
        "week_study": str,
    },
)

ScheduleDict = TypedDict(
    "ScheduleDict",
    {
        "room": str,
        "subject": str,
        "lhp": str,
        "periods": str,
        "period_detail": str,
        "time": str,
        "teacher": str,
    },
)
