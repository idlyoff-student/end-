total_sum = 0
number = 0

while number != 100:
    number = int(input("Введите число (100 для завершения): "))
    if number != 100: 
        total_sum += number

print("Сумма введенных чисел:", total_sum)
