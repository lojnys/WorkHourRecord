import unittest
import sys

sys.path.append("/Users/yushinnam/Desktop/python3/WorkHourRecord/model")

from WorkTime import WorkTime


class WorkTimeTest(unittest.TestCase):

    def setUp(self):
        self.work = WorkTime(15.5, 20, "2023-06-23")

    def test_init(self):

        self.assertEqual(self.work.getHours(), 15.5)
        self.assertEqual(self.work.getRate(), 20)
        self.assertEqual(self.work.getDate(), "2023-06-23")


    
    def test_setHours(self):
        self.work.setHours(20.0)

        self.assertEqual(self.work.getHours(), 20.0)

    
    def test_setRate(self):
        self.work.setRate(25)

        self.assertEqual(self.work.getRate(), 25)


    def test_setDate(self):
        self.work.setDate("2023-06-24")

        self.assertEqual(self.work.getDate(), "2023-06-24")


    def test_addToJSON(self):

        dict = self.work.addToJSON()

        self.assertEqual(dict, {'hours': 15.5, "rate": 20, "date": "2023-06-23"})
        self.assertEqual(dict['hours'], 15.5)
        self.assertEqual(dict['rate'], 20)
        self.assertEqual(dict['date'], '2023-06-23')


if __name__ == "__main__":
    unittest.main()