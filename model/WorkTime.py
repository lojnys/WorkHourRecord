import datetime as dt

class WorkTime():
    

    # work time slot is created with given hours, rate, and any notes
    def __init__(self, hours: float, rate: float, note: str, date) -> None:
        self.hours = hours
        self.rate = rate
        self.note = note
        self.date = date


    # returns each hour, rate, and note
    def getHours(self) -> float:
        return self.hours
    
    def getRate(self) -> float:
        return self.rate
    
    def getNote(self) -> str:
        return self.note
    
    def getDate(self):
        return self.date
    
    # sets each hours, rate, and note with given values
    def setHours(self, hours: float) -> None:
        self.hours = hours

    def setRate(self, rate: float) -> None:
        self.rate = rate

    def setNote(self, note: str) -> None:
        self.note = note

    def setDate(self, date) -> None:
        self.date = date


    def addToJSON(self) -> dict:
        input = {
            "hours": float(self.hours),
            "rate": float(self.rate),
            "note": self.note,
            "date": self.date
        }
        return input