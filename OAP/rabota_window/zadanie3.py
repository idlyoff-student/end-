from tkinter import *

window = Tk()

frame_top = Frame(window)
frame_bot = Frame(window)

lab_1 = Label(frame_top, width=8, height=3, bg='yellow', text="1")
lab_2 = Label(frame_top, width=8, height=3, bg='red', text="2")
lab_3 = Label(frame_bot, width=8, height=3, bg='lightgreen', text="3")
lab_4 = Label(frame_bot, width=8, height=3, bg='lightblue', text="4")

frame_top.pack()
frame_bot.pack()

lab_1.pack(side=LEFT)
lab_2.pack(side=LEFT)
lab_3.pack(side=LEFT)
lab_4.pack(side=LEFT)

window.mainloop()
