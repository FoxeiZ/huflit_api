DAYNAME_MAPPING = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)
REVERSED_DAYNAME_MAPPING = (
    "Thứ 2",
    "Thứ 3",
    "Thứ 4",
    "Thứ 5",
    "Thứ 6",
    "Thứ 7",
    "Chủ Nhật",
)


def from_str(day: str) -> str:
    if day == "Chủ Nhật":
        return DAYNAME_MAPPING[-1]

    return DAYNAME_MAPPING[int(day.strip()[-1]) - 2]


def reverse_from_str(day: str):
    return REVERSED_DAYNAME_MAPPING[DAYNAME_MAPPING.index(day)]


def from_int(day: int) -> str:
    return DAYNAME_MAPPING[day - 2]


def reverse_from_int(day: int):
    return REVERSED_DAYNAME_MAPPING[day - 2]
