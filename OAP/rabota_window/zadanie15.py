from tkinter import *
import tkinter.messagebox as box

# Функция по выводу диалогового окна
def dialog():
    box.showinfo("Выбор языка", "Вы выбрали язык " + listbox.get(listbox.curselection()))

# Создаем окно
window = Tk()
window.title("Работа со списком")  # Заголовок окна

# Создаем фрейм для виджетов
frame = Frame(window)

# Создаем виджет Listbox
listbox = Listbox(frame)

# Заполняем список
for i in ('Java', 'C++', 'Python', 'C#', 'JavaScript', 'PHP'):
    listbox.insert(END, i)
listbox.insert(3, "FORTRAN")  # Вставляем FORTRAN на 4-ю позицию

# Создаем кнопку
btn = Button(frame, text="Выберите язык", bg="lightgreen", command=dialog)

# Размещаем виджеты
btn.pack(side=RIGHT, padx=15)
listbox.pack(side=LEFT)
frame.pack(padx=30, pady=30)

# Цикл обработки событий окна
window.mainloop()
