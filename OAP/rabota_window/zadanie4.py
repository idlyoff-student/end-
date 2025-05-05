from tkinter import *

window = Tk()
window.title("Вывод текста")
window.geometry("500x300")

label = Label(window, bg="blue", fg="yellow", text="СПБГАСУ", font="Arial 16")

# Размещаем метку в окне
label.pack()  # Размещаем метку в окне по вертикали — вверху, по горизонтали — посередине
label.pack(expand=1)  # Размещаем метку в окне по вертикали — посередине, по горизонтали — посередине
label.pack(expand=1, fill=X)  # Заполняем всё пространство по горизонтали
label.pack(expand=1, fill=BOTH)  # Заполняем всё пространство по обеим осям
label.pack(anchor=NW)  # Размещаем метку с текстом в левом верхнем углу

window.mainloop()
