from math import *

def f1(a, x):
    y = (tan(x**2 / 2 - 1)**2 + (2 * cos(x - pi / 6)) / (1 / 2 + sin(a)**2))
    return y

def f2(x):
    y = pow(2, log(3 - cos(pi / 4 + 2 * x), 3 + sin(x)) / (1 + tan(2 * x / pi)**2))
    return y

try:
    fi = open("lab1_pb_in.txt", "rt")
except FileNotFoundError:
    print("Входной файл 'lab1_pb_in.txt' не найден. Создаю новый файл с примерными данными.")
    with open("lab1_pb_in.txt", "wt") as fi:
        fi.write("1.0 0.5\n")
        fi.write("2.0 1.0\n")
        fi.write("3.0 1.5\n")
    fi = open("lab1_pb_in.txt", "rt")

try:
    fo = open("lab1_pb_ou.txt", "wt")
except IOError:
    print("Ошибка: Не удалось открыть выходной файл 'lab1_pb_ou.txt'.")
    fi.close()
    exit(1)

line = fi.readline()
fo.write("+======+======+=========+========+\n")
fo.write("I A I X I F1 I F2 I\n")
fo.write("+======+======+=========+========+\n")

for line in fi:
    if line == "\n":
        continue
    (b, c) = line.split()
    a = float(b)
    x = float(c)
    fo.write("I {0: .1f} I {1: .1f} I {2: 5.4f} I".format(a, x, f1(a, x)))
    fo.write("{0: 6.4f} I\n".format(f2(x)))
    fo.write("+------+------+---------+--------+\n")

fi.close()
fo.close()
