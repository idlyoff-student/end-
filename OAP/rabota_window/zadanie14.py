from tkinter import *

# Создаем окно
window = Tk()
window.title("Полоса прокрутки")  # Заголовок окна

# Создаем многострочное поле ввода
text = Text(width=30, height=5, bg="blue", fg="yellow", wrap=WORD)
text.pack(side=LEFT)

# Создаем вертикальную полосу прокрутки
scroll = Scrollbar(orient=VERTICAL, command=text.yview)
scroll.pack(side=RIGHT, fill=Y)

# Конфигурируем поле ввода с полосой прокрутки
text.config(yscrollcommand=scroll.set)

window.mainloop()
