from tkinter import *

def color_switch():
    if window.cget("bg") == "yellow":
        window.configure(bg="green")
    else:
        window['bg'] = "yellow"

window = Tk()
window.title("Работа с кнопками")
window.geometry("500x300")

btn_exit = Button(window, text="Выход", bg="#ff0000", fg="green", width=12, command=exit)
btn_switch = Button(window, text="Цвет окна", bg="blue", fg="red", width=15, font=("Arial", 16, "bold"), command=color_switch)

btn_switch.pack(padx=150, pady=50)
btn_exit.pack(padx=150, pady=20)

window.mainloop()
