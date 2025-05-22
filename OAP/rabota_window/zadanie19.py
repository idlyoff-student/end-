from tkinter import *

# Создаем окно
window = Tk()
window.title("Меню с выпадающим списком")

# Создаем меню в главном окне
mainmenu = Menu(window)
window.config(menu=mainmenu)

# Создаем пункты подменю для пункта меню "Файл"
filemenu = Menu(mainmenu, tearoff=0)  # Создаем еще один объект Menu
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход", command=window.quit)  # Добавлена команда для выхода

# Создаем пункты подменю для пункта меню "Справка"
helpmenu = Menu(mainmenu, tearoff=0)  # Создаем еще один объект Menu
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")

# Связываем два созданных меню с главным меню
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

# Цикл обработки событий окна
window.mainloop()
