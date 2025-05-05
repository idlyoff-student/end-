from tkinter import *

class My_Button:
    def __init__(self, mwindow, mtext="Цвет окна", mwidth=15, mheight=3, mbg="blue", mfg="red", mpdx=150, mpdy=50):
        self.btn = Button(mwindow, text=mtext, width=mwidth, height=mheight, bg=mbg, fg=mfg)
        self.btn.pack(padx=mpdx, pady=mpdy)

    def setFunc(self, func):
        self.btn['command'] = eval('self.' + func)

    def color_change(self):
        if window.cget("bg") == "yellow":  # Исправлено на '=='
            window.configure(bg="green")
        else:
            window['bg'] = "yellow"

    def m_exit(self):
        exit()

window = Tk()
window.title("Работа с кнопками")
window.geometry("500x300")

btn_switch = My_Button(window)
btn_switch.setFunc('color_change')

btn_exit = My_Button(window, "Выход", 12, 3, "#ff0000", "green", 150, 20)
btn_exit.setFunc('m_exit')

window.mainloop()
