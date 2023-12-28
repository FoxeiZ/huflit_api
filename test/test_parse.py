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
                    "Tuesday": [
                        {
                            "lhp": "111111111111",
                            "subject": "Lập trình trên thiết bị di động",
                            "credits": "4",
                            "class_id": "T22101",
                            "time": "9:30 - 12:00",
                            "room": "PM04",
                            "teacher": "Teacher1",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "lhp": "111111111111",
                            "subject": "Lập trình trên thiết bị di động",
                            "credits": "4",
                            "class_id": "T22203",
                            "time": "12:45 - 15:15",
                            "room": "B46",
                            "teacher": "Teacher1",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                    ],
                    "Wednesday": [
                        {
                            "lhp": "111111111111",
                            "subject": "Tư tưởng Hồ Chí Minh",
                            "credits": "2",
                            "class_id": "NB2204",
                            "time": "10:25 - 12:00",
                            "room": "B47",
                            "teacher": "Teacher2",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "lhp": "111111111111",
                            "subject": "Phân tích và thiết kế phần mềm",
                            "credits": "4",
                            "class_id": "T22102",
                            "time": "12:45 - 15:15",
                            "room": "PM03",
                            "teacher": "Teacher3",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "lhp": "111111111111",
                            "subject": "Mạng máy tính",
                            "credits": "4",
                            "class_id": "T22108",
                            "time": "15:30 - 18:00",
                            "room": "B54",
                            "teacher": "Teacher4",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                    ],
                    "Thursday": [
                        {
                            "lhp": "111111111111",
                            "subject": "Đại cương pháp luật Việt Nam",
                            "credits": "2",
                            "class_id": "T22107",
                            "time": "10:25 - 12:00",
                            "room": "B36",
                            "teacher": "Teacher5, Teacher6",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "lhp": "111111111111",
                            "subject": "Lý thuyết đồ thị",
                            "credits": "3",
                            "class_id": "T22204",
                            "time": "15:30 - 18:00",
                            "room": "PM18",
                            "teacher": "Teacher7",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                    ],
                    "Friday": [
                        {
                            "lhp": "111111111111",
                            "subject": "Lý thuyết đồ thị",
                            "credits": "3",
                            "class_id": "T22202",
                            "time": "10:25 - 12:00",
                            "room": "B21",
                            "teacher": "Teacher8",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "lhp": "111111111111",
                            "subject": "Lý thuyết đồ thị",
                            "credits": "3",
                            "class_id": "T22202",
                            "time": "10:25 - 12:00",
                            "room": "B34",
                            "teacher": "Teacher8",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "lhp": "111111111111",
                            "subject": "Phân tích và thiết kế phần mềm",
                            "credits": "4",
                            "class_id": "T22201",
                            "time": "12:45 - 15:15",
                            "room": "B21",
                            "teacher": "Teacher3",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                        {
                            "lhp": "111111111111",
                            "subject": "Phân tích và thiết kế phần mềm",
                            "credits": "4",
                            "class_id": "T22201",
                            "time": "12:45 - 15:15",
                            "room": "C11",
                            "teacher": "Teacher3",
                            "week_study": "(01/01/1990->01/01/1990)",
                        },
                    ],
                    "Saturday": [
                        {
                            "lhp": "111111111111",
                            "subject": "Mạng máy tính",
                            "credits": "4",
                            "class_id": "",
                            "time": " Bảy",
                            "room": "4 - 6",
                            "teacher": "PM21",
                            "week_study": "Teacher9",
                        }
                    ],
                },
            )


if __name__ == "__main__":
    unittest.main()
