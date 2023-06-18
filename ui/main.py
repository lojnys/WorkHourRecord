import tkinter as tk
import json

import sys
sys.path.append("/Users/yushinnam/Desktop/python3/WorkHourRecord/model")

from WorkTime import WorkTime
from WorkTimes import WorkTimes
from BiWeekly import BiWeekly


with open("/Users/yushinnam/Desktop/python3/WorkHourRecord/data/data.json") as file:
    data = json.load(file)


weeks = BiWeekly()
weeks.setLists(data["bi-weekly"])
works = WorkTimes()
# print(weeks.getLists())
# print(weeks.getLists()[0].addAmount())
# print(weeks.getLists()[0].getList()[0].getHours())


def setWeek():
    global works

    for week in weeks.getLists():
        if display.get(display.curselection()) == week.getDate():
            works = week
            # print(works.getList())
            # works.setList(data["bi-weekly"][display.curselection()[0]][week.getDate()])

    welcome.config(text="Week Set!")
    window.after(3000, lambda : welcome.config(text="Welcome"))

        

def addAmount():
    welcome.config(text=f"$ {works.addAmount()}")
    print(f"$ {works.addAmount()}")





# making the overall window
window = tk.Tk()
window.geometry("450x300+800+300")
window.title("Work Hour Record")


# three main parts within the windwo
displayFrame = tk.Frame(window)
display = tk.Listbox(displayFrame, selectmode="single")
welcomeFrame = tk.Frame(window)
welcome = tk.Label(welcomeFrame, text="Welcome")
welcomeFrame.pack(side='top')
displayFrame.pack()
welcome.pack()
display.pack()

# inserting the weeks into the display window
for week in weeks.getLists():
    display.insert(-1, week.getDate())


# buttons and labels of the lowest frame
frame2 = tk.Frame(window)
frame3 = tk.Frame(frame2)
hourLabel = tk.Label(frame3, text='Hours')
rateLabel = tk.Label(frame3, text='Rate')
dateLabel = tk.Label(frame3, text='Date')
hourEntry = tk.Entry(frame3, width=7)
rateEntry = tk.Entry(frame3, width=7)
dateEntry = tk.Entry(frame3, width=7)
addButton = tk.Button(frame3, text="Add")
amountButton = tk.Button(frame2, text="Add Amount", command=addAmount)
setButton = tk.Button(frame2, text="Set Week", command=setWeek)


hourLabel.pack(side='left')
hourEntry.pack(side='left')
rateLabel.pack(side='left')
rateEntry.pack(side='left')
dateLabel.pack(side='left')
dateEntry.pack(side='left')
addButton.pack(side='left')
frame3.pack(side='top')
amountButton.pack(side='right')
setButton.pack(side='left')
frame2.pack(side='bottom')


window.mainloop()