from tkinter import *

# Создаем окно
window = Tk()
window.title("Работа с меню")  # Заголовок окна

# Создаем меню в главном окне
mainmenu = Menu(window)

# Добавляем пункты меню
mainmenu.add_command(label="Файл", command=lambda: print("Выбран пункт 'Файл'"))  # Добавлен пример команды
mainmenu.add_command(label="Справка", command=lambda: print("Выбран пункт 'Справка'"))  # Добавлен пример команды

# Конфигурируем окно с меню
window.config(menu=mainmenu)

# Цикл обработки событий окна
window.mainloop()
