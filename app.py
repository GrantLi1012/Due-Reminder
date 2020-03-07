import json
import os
import tkinter as tk
from tkinter import *


def remove_task(lis):
    # remove task from file
    print(lis)

def add_task(typ, event, date, time):
    # add task to file
    print(typ)

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


