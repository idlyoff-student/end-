from tkinter import *

window = Tk()

lab_1 = Label(width=8, height=3, bg='yellow', text="1")
lab_2 = Label(width=8, height=3, bg='red', text="2")
lab_3 = Label(width=8, height=3, bg='lightgreen', text="3")
lab_4 = Label(width=8, height=3, bg='lightblue', text="4")

# Располагаем метки вертикально сверху вниз
lab_1.pack()
lab_2.pack()
lab_3.pack()
lab_4.pack()

# Пример расположения меток (выберите один из вариантов)
# lab_1.pack(side=BOTTOM)  
# lab_2.pack(side=BOTTOM) 
# lab_3.pack(side=BOTTOM) 
# lab_4.pack(side=BOTTOM) 

# lab_1.pack(side=LEFT)  
# lab_2.pack(side=LEFT) 
# lab_3.pack(side=LEFT) 
# lab_4.pack(side=LEFT) 

# lab_1.pack(side=RIGHT)  
# lab_2.pack(side=RIGHT) 
# lab_3.pack(side=RIGHT) 
# lab_4.pack(side=RIGHT) 

# lab_1.pack(side=BOTTOM)  
# lab_2.pack(side=TOP) 
# lab_3.pack(side=LEFT) 
# lab_4.pack(side=RIGHT) 

# lab_1.pack(side=LEFT)  
# lab_2.pack(side=LEFT) 
# lab_3.pack(side=BOTTOM)

window.mainloop()
