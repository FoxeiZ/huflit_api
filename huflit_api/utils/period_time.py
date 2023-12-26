MAPPING_START_TIME = (
    "6:45",
    "7:35",
    "8:25",
    "9:30",
    "10:25",
    "11:10",
    "12:45",
    "13:35",
    "14:25",
    "15:30",
    "16:25",
    "17:10",
    "18:15",
    "19:05",
    "19:55",
)

MAPPING_END_TIME = (
    "7:35",
    "8:25",
    "9:15",
    "10:25",
    "11:10",
    "12:00",
    "13:35",
    "14:25",
    "15:15",
    "16:25",
    "17:00",
    "18:00",
    "19:05",
    "19:55",
    "20:45",
)


def start_from_int(period: int) -> str:
    return MAPPING_START_TIME[period - 1]


def end_from_int(period: int) -> str:
    return MAPPING_END_TIME[period - 1]


def from_detail_periods(periods: str) -> tuple:
    start_index, end_index = map(int, periods.split("-"))
    return (
        MAPPING_START_TIME[start_index - 1],
        MAPPING_END_TIME[end_index - 1],
    )
