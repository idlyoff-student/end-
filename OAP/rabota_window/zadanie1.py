from tkinter import *

window = Tk()
window.title("Вывод текста")
window.geometry("500x300")

label = Label(window, text="Кафедра информационных технологий", font="Arial 16")
label.pack(side=TOP)

label_1 = Label(window, text="СПБГАСУ", font=("Arial", 24, "bold"))
label_1.pack(padx=150, pady=50)

window.mainloop()
