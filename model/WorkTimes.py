from WorkTime import WorkTime
from datetime import date

class WorkTimes():

    def __init__(self, list=[], date="") -> None:
        self.list = list
        self.date = date


    def getList(self) -> list:
        return self.list
    
    def getDate(self) -> str:
        return self.date
    
    def setList(self, list) -> None:
        self.list = [WorkTime(x["hours"], x["rate"], x['note'], x['date']) for x in list]

    def isEmpty(self) -> bool:
        return self.list == []

    def count(self) -> int:
        result = 0
        for x in self.list:
            result += 1

        return result

    def addWorkTime(self, workTime: WorkTime) -> None:
        self.list.append(workTime)

    def addAmount(self, note) -> float:
        result = 0
        for workTime in self.list:
            if note == workTime.getNote():
                result += workTime.getHours() * workTime.getRate()

        return result
    
    def addToJSON(self, date) -> dict:
        # result = []
        # for workTime in self.list:
        #     result.append(workTime.addToJSON())
        list = [workTime.addToJSON() for workTime in self.list]
        return {date: list}