from tkinter import *

window = Tk()
window.title("Изменение свойств заголовка окна")

btn = Button(window, bg="blue", fg="yellow", text="Запуск программы", font="Arial 16")

def change():
    btn['text'] = "Программа запущена..."
    btn['bg'] = '#000000'
    btn['fg'] = '#ffffff'

btn.configure(command=change)
btn.pack()

window.mainloop()
