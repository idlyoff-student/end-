from tkinter import *
from tkinter import filedialog as fd

def insertText():
    file_name = fd.askopenfilename()  # Получаем имя файла
    with open(file_name, 'r') as f:  # Открываем файл для чтения
        s = f.read()  # Считываем информацию из файла
        text.insert(1.0, s)  # Вставляем информацию в текстовое поле

def extractText():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"), 
                                                 ("HTML files", "*.html;*.htm"), 
                                                 ("All files", "*.*")))  # Получаем имя файла, в который надо сохранить информацию
    with open(file_name, 'w') as f:  # Открываем файл для записи
        s = text.get(1.0, END)  # Считываем информацию из текстового поля
        f.write(s)  # Записываем считанную информацию в файл

window = Tk()  # Создаем окно
text = Text(width=50, height=25)
text.grid(columnspan=2)

b1 = Button(text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)

b2 = Button(text="Сохранить", command=extractText)
b2.grid(row=1, column=1, sticky=W)

window.mainloop()  # Цикл обработки событий окна
