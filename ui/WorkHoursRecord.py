import tkinter as tk
from tkinter import messagebox
import json
import time

import sys
sys.path.append("/Users/yushinnam/Desktop/python3/WorkHourRecord/model")

from WorkTime import WorkTime
from WorkTimes import WorkTimes
from BiWeekly import BiWeekly


filename = "/Users/yushinnam/Desktop/python3/WorkHourRecord/data/data.json"

with open(filename) as file:
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
    # welcome.after(3000, welcome.config(text="Welcome"))

        

def addAmount():

    notes = set([work.getNote() for work in works.getList()])
    printable_notes = [(note, works.addAmount(note)) for note in notes]
    
    printable_string = ""
    for pair in printable_notes:
        string = pair[0] + ": $" + str(pair[1]) + " "
        printable_string += string
    
    welcome.config(text=printable_string)



def addWork():
    hour = float(hourEntry.get())
    rate = float(rateEntry.get())
    note = noteEntry.get()
    date = dateEntry.get()
    work = WorkTime(hour, rate, note, date)
    works.addWorkTime(work)
    hourEntry.delete(0, tk.END)
    rateEntry.delete(0, tk.END)
    noteEntry.delete(0, tk.END)
    dateEntry.delete(0, tk.END)

    weeks.addToJSON()


def addWeek():

    def on_click():
        date = dateEntry.get()
        week = WorkTimes([], date)
        weeks.addList(week)
        dateEntry.delete(0, tk.END)

        weeks.addToJSON()

        list.append(date)
        displayList.set(list)


    week_window = tk.Tk()
    week_window.geometry("+900+400")
    week_window.title("Week Add")

    dateEntry = tk.Entry(week_window)
    weekAddButton = tk.Button(week_window, text="Add", command=on_click)

    dateEntry.pack(side='left')
    weekAddButton.pack(side='right')

    week_window.mainloop()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


# ==========================================================================================

# making the overall window
window = tk.Tk()
window.geometry("450x300+800+300")
window.title("Work Hour Record")


# inserting the weeks into the display window
list = [x.getDate() for x in weeks.getLists()]
displayList = tk.StringVar(value=list)

# three main parts within the windwo
displayFrame = tk.Frame(window)
display = tk.Listbox(displayFrame, selectmode="single", listvariable=displayList)
scrollbar = tk.Scrollbar(displayFrame)
display.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=display.yview)

welcomeFrame = tk.Frame(window)
welcome = tk.Label(welcomeFrame, text="Welcome")

welcomeFrame.pack(side='top')
displayFrame.pack()
welcome.pack()
display.pack(side=tk.LEFT)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)


# buttons and labels of the lowest frame
frame2 = tk.Frame(window)
frame3 = tk.Frame(frame2)
frame4 = tk.Frame(frame2)

hourLabel = tk.Label(frame3, text='Hours')
rateLabel = tk.Label(frame3, text='Rate')
dateLabel = tk.Label(frame3, text='Date')
noteLabel = tk.Label(frame4, text='Note')
hourEntry = tk.Entry(frame3, width=7)
rateEntry = tk.Entry(frame3, width=7)
dateEntry = tk.Entry(frame3, width=7)
noteEntry = tk.Entry(frame4, width=15)

addButton = tk.Button(frame3, text="Add", command=addWork)
amountButton = tk.Button(frame2, text="Add Amount", command=addAmount)
setButton = tk.Button(frame2, text="Set Week", command=setWeek)
addWorks = tk.Button(frame2, text="Add Week", command=addWeek)

noteLabel.pack(side='left')
noteEntry.pack(side='right')
hourLabel.pack(side='left')
hourEntry.pack(side='left')
rateLabel.pack(side='left')
rateEntry.pack(side='left')
dateLabel.pack(side='left')
dateEntry.pack(side='left')
addButton.pack(side='left')
frame4.pack(side='top')
frame3.pack(side='top')
amountButton.pack(side='right')
setButton.pack(side='left')
addWorks.pack()
frame2.pack(side='bottom')


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()