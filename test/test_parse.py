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


if __name__ == "__main__":
    unittest.main()
