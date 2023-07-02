import unittest
import sys

sys.path.append("/Users/yushinnam/Desktop/python3/WorkHourRecord/model")

from WorkTime import WorkTime
from WorkTimes import WorkTimes


unittest.TestLoader.sortTestMethodsUsing = None

class WorkTimesTest(unittest.TestCase):

    
    def setUp(self) -> None:
        self.worktimes = WorkTimes()
        self.worktime = WorkTime(25, 25, "2023-07-01")


    def test_init(self):
        self.assertEqual(self.worktimes.count(), 3)
        self.assertEqual(self.worktimes.getDate(), "")

    
    def test_setters(self) -> None:
        self.worktimes.setList([{"hours": 10, "rate": 25, "date": ""}])
        self.assertEqual(self.worktimes.getList()[0].getHours(), 10)
        self.assertEqual(self.worktimes.getList()[0].getRate(), 25)
        self.assertEqual(self.worktimes.getList()[0].getDate(), "")


    def test_addWorkTime(self) -> None:
        self.worktimes.addWorkTime(self.worktime)

        self.assertFalse(self.worktimes.isEmpty())
        # self.assertEqual(self.worktimes.count(), 1)
        self.assertEqual(self.worktimes.getList()[0].getHours(), self.worktime.getHours())
        self.assertEqual(self.worktimes.getList()[0].getRate(), self.worktime.getRate())
        self.assertEqual(self.worktimes.getList()[0].getDate(), self.worktime.getDate())

    
    def test_addAmount(self) -> None:
        self.worktimes.addWorkTime(self.worktime)
        self.assertEqual(self.worktimes.addAmount(), 625)

        self.worktimes.addWorkTime(WorkTime(12.5, 20, "2023-06-30"))
        self.assertEqual(self.worktimes.addAmount(), 875)



if __name__ == "__main__":
    unittest.main()