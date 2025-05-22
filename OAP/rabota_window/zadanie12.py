from tkinter import *

# Создаем окно
window = Tk()
window.title("Многострочный заголовок окна")  # Заголовок окна

# Функция для вставки текста
def insertText():
    s = "Кафедра информационных технологий"
    text.insert(1.0, s)

# Функция для считывания текста
def getText():
    s = text.get(2.0, 2.7)
    label['text'] = s

# Функция для удаления текста
def deleteText():
    text.delete(2.8, END)

# Создаем многострочное текстовое поле
text = Text(width=25, height=5)
text.pack()

# Создаем фрейм
frame = Frame(window)
frame.pack()

# Создаем три кнопки
b_insert = Button(frame, text="Вставить текст", command=insertText)
b_insert.pack(side=LEFT)

b_get = Button(frame, text="Считать текст", command=getText)
b_get.pack(side=LEFT)

b_delete = Button(frame, text="Удалить текст", command=deleteText)
b_delete.pack(side=LEFT)

# Создаем метку для вывода текста
label = Label(window)  # Добавлено окно в качестве родителя
label.pack()

# Цикл обработки событий окна
window.mainloop()
