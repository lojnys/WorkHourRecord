import json
from WorkTimes import WorkTimes

class BiWeekly():
    
    def __init__(self, lists=[]) -> None:
        self.lists = lists

    def getLists(self) -> list:
        return self.lists
    
    def setLists(self, lists) -> None:
        # self.list = list(map(lists, lambda x: WorkTimes(list(x.values())[0])))
        result = []
        for works in lists:
            work_list = list(works.values())[0]
            work_date = list(works.keys())[0]
            work_list_object = WorkTimes(work_list, work_date)
            work_list_object.setList(work_list)
            result.append(work_list_object)
        self.lists = result

    def addList(self, list) -> None:
        self.lists.append(list)


    def addToJSON(self) -> None:
        list = [x.addToJSON(x.getDate()) for x in self.lists]
        dict = {"bi-weekly": list}

        with open("/Users/yushinnam/Desktop/python3/WorkHourRecord/data/data.json", "w") as file:
            json.dump(dict, file)