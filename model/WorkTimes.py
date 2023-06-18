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
        # self.list = list(map(list, lambda x: WorkTime(x["hours"], x["rate"], x["note"], x["date"])))
        self.list = [WorkTime(x["hours"], x["rate"], x["note"], x['date']) for x in list]

    
    def addWorkTime(self, workTime: WorkTime) -> None:
        self.list.append(workTime)

    def removeWorkTime(self, workTime: WorkTime) -> None:
        pass

    def addAmount(self) -> float:
        result = 0
        for workTime in self.list:
            result += workTime.getHours() * workTime.getRate()

        return result
    
    def addToJSON(self, date) -> dict:
        # result = []
        # for workTime in self.list:
        #     result.append(workTime.addToJSON())
        list = [workTime.addToJSON() for workTime in self.list]
        return {date: list}