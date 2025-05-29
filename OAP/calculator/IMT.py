import tkinter as tk
from tkinter import ttk

BMI_TABLE = {
    1: [14.6, 15.4, 17.2, 19.4, 19.9],  # [Критически недостаточный, Недостаточный, Норма, Лишний, Ожирение]
    2: [14.4, 15.0, 16.5, 18.4, 19.0],
    3: [14.0, 14.6, 16.0, 17.8, 18.4],
    4: [13.8, 14.4, 15.8, 17.5, 18.1],
    5: [13.7, 14.2, 15.5, 17.3, 18.0],
    6: [13.6, 14.0, 15.4, 17.4, 18.1],
    7: [13.6, 14.0, 15.5, 17.7, 18.9],
    8: [12.5, 14.2, 16.4, 19.3, 22.6],
    9: [12.8, 13.7, 17.1, 19.4, 21.6],
    10: [13.9, 14.6, 17.1, 21.4, 25.0],
    11: [14.0, 14.3, 17.8, 21.2, 23.1],
    12: [14.6, 14.8, 18.4, 22.0, 24.8],
    13: [15.6, 16.2, 19.1, 21.7, 24.5],
    14: [16.1, 16.7, 19.8, 22.6, 25.7],
    15: [17.0, 17.8, 20.2, 23.1, 25.9],
    16: [17.8, 18.5, 21.0, 23.7, 26.0],
    17: [17.6, 18.6, 21.6, 23.7, 25.8],
}

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Кулешов Олег Сергеевич")
        self.master.geometry("400x300")

        # Labels
        self.height_label = ttk.Label(self.master, text="Рост (см):")
        self.weight_label = ttk.Label(self.master, text="Вес (кг):")
        self.age_label = ttk.Label(self.master, text="Возраст (лет):")

        # Entry fields
        self.height_entry = ttk.Entry(self.master, width=15)
        self.weight_entry = ttk.Entry(self.master, width=15)
        self.age_entry = ttk.Entry(self.master, width=15)

        # Button
        self.calculate_button = ttk.Button(self.master, text="Вычислить ИМТ", command=self.calculate_bmi)

        # Result Label
        self.result_label = ttk.Label(self.master, text="")

        # Grid layout
        self.height_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)

        self.weight_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        self.age_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.age_entry.grid(row=2, column=1, padx=10, pady=10)

        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get()) / 100
            weight = float(self.weight_entry.get())
            age = int(self.age_entry.get())

            if height <= 0 or weight <= 0 or age <= 0:
                self.result_label.config(text="Введите корректные значения роста, веса и возраста.")
                return

            bmi = weight / (height ** 2)
            bmi = round(bmi, 2)

            if 1 <= age <= 17:
                # Классификация ИМТ для детей (с использованием таблицы)
                if age in BMI_TABLE:
                    bmi_limits = BMI_TABLE[age]  # [Критически недостаточный, Недостаточный, Норма, Лишний, Ожирение]

                    if bmi < bmi_limits[0]:
                        category = "Критически недостаточный вес"
                    elif bmi < bmi_limits[1]:
                        category = "Недостаточный вес"
                    elif bmi <= bmi_limits[2]:
                        category = "Нормальный вес"
                    elif bmi <= bmi_limits[3]:
                        category = "Лишний вес"
                    else:
                        category = "Ожирение"
                else:
                    category = "Нет данных для этого возраста."
                    # **Важно:** В реальном коде нужно интерполировать или экстраполировать
                    # значения ИМТ для возраста, если его нет в таблице.
            else:
                category = "Данные только для детей от 1 до 17 лет."

            result_text = f"Ваш ИМТ: {bmi}\nВозраст: {age}\nКатегория: {category}"
            self.result_label.config(text=result_text)

        except ValueError:
            self.result_label.config(text="Введите числовые значения для роста, веса и возраста.")

if __name__ == '__main__':
    root = tk.Tk()
    bmi_calc = BMI_Calculator(root)
    root.mainloop()

