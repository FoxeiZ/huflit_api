import os
import unittest

from huflit_api import PortalParser

TESTDATA_DIR = os.path.join(os.path.dirname(__file__), "testdata")


class TestParse(unittest.TestCase):
    def test_notification(self):
        pass

    def test_schedule(self):
        with open(TESTDATA_DIR + "/DrawingSchedules.html") as f:
            html = f.read()
            self.assertDictEqual(
                PortalParser.parse_schedule(html),
                {
                    "Wednesday": [
                        {
                            "room": "B47",
                            "subject": "Class 1 (1111111)",
                            "lhp": "-1",
                            "periods": "2",
                            "period_detail": "5-6",
                            "time": "10:25 - 12:00",
                            "teacher": "TeacherName1",
                        },
                        {
                            "room": "B54",
                            "subject": "Class 6 (1111111)",
                            "lhp": "-1",
                            "periods": "3",
                            "period_detail": "10-12",
                            "time": "15:30 - 18:00",
                            "teacher": "TeacherName6",
                        },
                    ],
                    "Thursday": [
                        {
                            "room": "B36",
                            "subject": "Class 2 (1111111)",
                            "lhp": "-1",
                            "periods": "2",
                            "period_detail": "5-6",
                            "time": "10:25 - 12:00",
                            "teacher": "TeacherName2",
                        }
                    ],
                    "Friday": [
                        {
                            "room": "B21",
                            "subject": "Class 3 (1111111)",
                            "lhp": "-1",
                            "periods": "2",
                            "period_detail": "5-6",
                            "time": "10:25 - 12:00",
                            "teacher": "TeacherName3",
                        },
                        {
                            "room": "B21",
                            "subject": "Class 5 (1111111)",
                            "lhp": "-1",
                            "periods": "3",
                            "period_detail": "7-9",
                            "time": "12:45 - 15:15",
                            "teacher": "TeacherName5",
                        },
                    ],
                    "Tuesday": [
                        {
                            "room": "B46",
                            "subject": "Class 4 (1111111)",
                            "lhp": "-1",
                            "periods": "3",
                            "period_detail": "7-9",
                            "time": "12:45 - 15:15",
                            "teacher": "TeacherName4",
                        }
                    ],
                },
            )

    def test_semester(self):
        with open(TESTDATA_DIR + "/DrawingStudentSchedule_Perior.html") as f:
            html = f.read()
            self.assertDictEqual(
                PortalParser.parse_semester(html),
                {
                    "Friday": [
                        {
                            "class_id": "T22202",
                            "credits": "3",
                            "lhp": "111111111111",
                            "period_detail": "5 - 6",
                            "room": "B21",
                            "subject": "Lý thuyết đồ thị",
                            "teacher": "Teacher8",
                            "time": "10:25 - 12:00",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "class_id": "T22202",
                            "credits": "3",
                            "lhp": "111111111111",
                            "period_detail": "5 - 6",
                            "room": "B34",
                            "subject": "Lý thuyết đồ thị",
                            "teacher": "Teacher8",
                            "time": "10:25 - 12:00",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "class_id": "T22201",
                            "credits": "4",
                            "lhp": "111111111111",
                            "period_detail": "7 - 9",
                            "room": "B21",
                            "subject": "Phân tích và thiết kế phần mềm",
                            "teacher": "Teacher3",
                            "time": "12:45 - 15:15",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "class_id": "T22201",
                            "credits": "4",
                            "lhp": "111111111111",
                            "period_detail": "7 - 9",
                            "room": "C11",
                            "subject": "Phân tích và thiết kế phần mềm",
                            "teacher": "Teacher3",
                            "time": "12:45 - 15:15",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                    ],
                    "Saturday": [
                        {
                            "class_id": "",
                            "credits": "4",
                            "lhp": "111111111111",
                            "period_detail": "4 - 6",
                            "room": "PM21",
                            "subject": "Mạng máy tính",
                            "teacher": "Teacher9",
                            "time": "9:30 - 12:00",
                            "week_study": "(01/01/1990->01/01/1990)",
                        }
                    ],
                    "Thursday": [
                        {
                            "class_id": "T22107",
                            "credits": "2",
                            "lhp": "111111111111",
                            "period_detail": "5 - 6",
                            "room": "B36",
                            "subject": "Đại cương pháp luật Việt Nam",
                            "teacher": "Teacher5, Teacher6",
                            "time": "10:25 - 12:00",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "class_id": "T22204",
                            "credits": "3",
                            "lhp": "111111111111",
                            "period_detail": "10 - 12",
                            "room": "PM18",
                            "subject": "Lý thuyết đồ thị",
                            "teacher": "Teacher7",
                            "time": "15:30 - 18:00",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                    ],
                    "Tuesday": [
                        {
                            "class_id": "T22101",
                            "credits": "4",
                            "lhp": "111111111111",
                            "period_detail": "4 - 6",
                            "room": "PM04",
                            "subject": "Lập trình trên thiết bị di động",
                            "teacher": "Teacher1",
                            "time": "9:30 - 12:00",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "class_id": "T22203",
                            "credits": "4",
                            "lhp": "111111111111",
                            "period_detail": "7 - 9",
                            "room": "B46",
                            "subject": "Lập trình trên thiết bị di động",
                            "teacher": "Teacher1",
                            "time": "12:45 - 15:15",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                    ],
                    "Wednesday": [
                        {
                            "class_id": "NB2204",
                            "credits": "2",
                            "lhp": "111111111111",
                            "period_detail": "5 - 6",
                            "room": "B47",
                            "subject": "Tư tưởng Hồ Chí Minh",
                            "teacher": "Teacher2",
                            "time": "10:25 - 12:00",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "class_id": "T22102",
                            "credits": "4",
                            "lhp": "111111111111",
                            "period_detail": "7 - 9",
                            "room": "PM03",
                            "subject": "Phân tích và thiết kế phần mềm",
                            "teacher": "Teacher3",
                            "time": "12:45 - 15:15",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "class_id": "T22108",
                            "credits": "4",
                            "lhp": "111111111111",
                            "period_detail": "10 - 12",
                            "room": "B54",
                            "subject": "Mạng máy tính",
                            "teacher": "Teacher4",
                            "time": "15:30 - 18:00",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                    ],
                },
            )


if __name__ == "__main__":
    unittest.main()
