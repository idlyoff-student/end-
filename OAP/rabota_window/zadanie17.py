from tkinter import *
import tkinter.messagebox as box

# Функция по выводу диалогового окна
def dialog():
    s = "Вы выбрали:"
    if var_1.get() == 1: s += "\nJava"
    if var_2.get() == 1: s += "\nC++"
    if var_3.get() == 1: s += "\nPython"
    if var_4.get() == 1: s += "\nFORTRAN"
    if var_5.get() == 1: s += "\nC#"
    if var_6.get() == 1: s += "\nJavaScript"
    if var_7.get() == 1: s += "\nPHP"
    box.showinfo("Выбор языка", s)

# Создаем окно
window = Tk()
window.title("Работа с флажками")  # Заголовок окна

# Создаем фрейм для виджетов
frame = Frame(window)
frame.pack(padx=20, pady=30)

# Создаем целочисленные переменные-объекты для хранения результата выбора
var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()
var_5 = IntVar()
var_6 = IntVar()
var_7 = IntVar()

# Создаем флажки
check_1 = Checkbutton(frame, text='Java', variable=var_1, onvalue=1, offvalue=0)
check_2 = Checkbutton(frame, text='C++', variable=var_2, onvalue=1, offvalue=0)
check_3 = Checkbutton(frame, text='Python', variable=var_3, onvalue=1, offvalue=0)
check_4 = Checkbutton(frame, text='FORTRAN', variable=var_4, onvalue=1, offvalue=0)
check_5 = Checkbutton(frame, text='C#', variable=var_5, onvalue=1, offvalue=0)
check_6 = Checkbutton(frame, text='JavaScript', variable=var_6, onvalue=1, offvalue=0)
check_7 = Checkbutton(frame, text='PHP', variable=var_7, onvalue=1, offvalue=0)

# Создаем кнопку
btn = Button(frame, text="Выбор языка", bg="lightgreen", command=dialog)

# Размещаем виджеты
btn.pack(side=RIGHT)
check_1.pack(side=LEFT)
check_2.pack(side=LEFT)
check_3.pack(side=LEFT)
check_4.pack(side=LEFT)
check_5.pack(side=LEFT)
check_6.pack(side=LEFT)
check_7.pack(side=LEFT)

# Цикл обработки событий окна
window.mainloop()
