from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title("Ввод данных")

frame = Frame(window)  # Создаем фрейм, в который будет размещено поле для ввода
entry = Entry(frame)  # Создаем поле ввода и привязываем его к фрейму

# Функция для отображения данных, считанных из поля ввода
def dialog():
    box.showinfo("Приветствие", "Привет, " + entry.get())  # Исправлено на entry

# Создаем кнопку, которая будет вызывать функцию dialog()
btn = Button(frame, text="Ввод", command=dialog)

# Создаем метку с поясняющим текстом
lb = Label(frame, text="Введите имя: ")

# Добавляем все виджеты на фрейм
lb.pack(side=LEFT)
entry.pack(side=LEFT)
btn.pack(side=RIGHT, padx=5)

frame.pack(padx=20, pady=20)

window.mainloop()  # Цикл обработки событий окна
