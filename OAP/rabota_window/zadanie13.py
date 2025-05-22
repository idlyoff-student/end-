from tkinter import *

# Создаем окно
window = Tk()
window.title("Форматирование заголовок окна")  # Заголовок окна

# Создаем многострочное текстовое поле
text = Text(width=45, height=10)
text.pack()

# Вставляем текст
text.insert(1.0, "Первая строка\nВторая строка\nТретья строка")  # Исправлено

# Форматируем первую строку
text.tag_add('first', 1.0, '1.end')
text.tag_config('first', font=("Verdana", 18, 'bold'), justify=CENTER)

# Форматируем вторую строку
text.tag_add('second', 2.0, '2.end')
text.tag_config('second', font=("Arial", 24, 'bold'), justify=RIGHT)

# Форматируем первое слово в третьей строке
text.tag_add('third', 3.0, '3.6')
text.tag_config('third', font=("Calibri", 12))

# Цикл обработки событий окна
window.mainloop()
