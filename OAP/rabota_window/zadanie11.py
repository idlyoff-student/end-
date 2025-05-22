from tkinter import *

# Создаем окно
window = Tk()
window.title("Многострочный текст")  # Заголовок окна

# Создаем многострочное поле ввода
text = Text(width=30, height=10, bg="blue", fg="yellow", wrap=WORD)
text.pack()

# Цикл обработки событий окна
window.mainloop()
