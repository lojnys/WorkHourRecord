import unittest
import sys

sys.path.append("/Users/yushinnam/Desktop/python3/WorkHourRecord/model")

from WorkTime import WorkTime
from WorkTimes import WorkTimes
from BiWeekly import BiWeekly


class BiWeeklyTest(unittest.TestCase):

    def setUp(self) -> None:
        self.biweekly = BiWeekly()