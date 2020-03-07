import json
import os
import tkinter as tk
from tkinter import *
from datetime import datetime


recent_task1 = StringVar()
recent_task2 = StringVar()
recent_task3 = StringVar()
recent_task4 = StringVar()
recent_task5 = StringVar()
recent_task6 = StringVar()
recent_task7 = StringVar()

recent_task_list = [recent_task1, recent_task2, recent_task3, recent_task4, recent_task5, recent_task6, recent_task7]
tmp = []


def delete_task(ty, ev):
    global tmp
    tmp = []
    tmp2 = []
    with open("tasks.txt", 'r') as open_file:
        tmp2 = json.load(open_file)
        for i in range(0, len(tmp2)):
            if not (tmp2[i]["Type"] == ty and tmp2[i]["Event"] == ev):
                tmp.append(tmp2[i])
        open_file.close()
    with open("tasks.txt", 'w') as write_file:
        json.dump(tmp, write_file)
        write_file.close()


def remove_tasks(lis):
    global recent_task_list
    rm_list = []
    with open('tasks.txt') as rm:
        rm_list = json.load(rm)
        for i in range(len(rm_list)):
            for j in range(len(lis)):
                if lis[j] is 1:
                    if recent_task_list[j]["Type"] == rm_list[i]["Type"] and recent_task_list[j]["Event"] == rm_list[i]["Event"]:
                        delete_task(recent_task_list[j]["Type"], recent_task_list[j]["Event"])
        rm.close()
    print(lis)


def add_task(typ, event, date, time):
    new_entry = {"Type": typ, "Event": event, "Date": date, "Time": time}
    with open('tasks.txt', 'rb+') as outfile:
        outfile.seek(-1, os.SEEK_END)
        outfile.truncate()
        outfile.close()

    with open('tasks.txt', 'a+') as outfile1:
        outfile1.write(",\n")
        outfile1.write(json.dumps(new_entry))
        outfile1.write("]")
        outfile1.close()


def get_task_list():
    target = []
    sorted_data = []
    with open('tasks.txt') as getTask:
        data = json.load(getTask)
        sorted_data = sorted(data, key=lambda x: datetime.strptime(x['Date'], '%m/%d/%Y'))
        getTask.close()
    if len(sorted_data) < 7:
        for i in range(0, len(sorted_data)):
            target[i] = sorted_data[i]
        for j in range(len(data), 7):
            target[j] = " "
    else:
        for k in range(0, 7):
            target[k] = sorted_data[k]
    return data


root = tk.Tk()
root.title("Reminder")

label1 = Label(root, text="Upcoming events").grid(row=0, column=0)
label2 = Label(root, text="Type: ").grid(row=9, column=0)
label3 = Label(root, text="Date: ").grid(row=10, column=0)
label4 = Label(root, text="Event: ").grid(row=9, column=2)
label5 = Label(root, text="Time: ").grid(row=10, column=2)

finished = [1, 2]
button1 = Button(root, text="Finished", command=lambda lis=finished: remove_task(lis)).grid(row=4, column=3)
button1 = Button(root, text="Add", command=lambda typ="type", event="event", date="date", time="time": add_task(typ, event, date, time)).grid(row=8, column=0)


root.mainloop()
