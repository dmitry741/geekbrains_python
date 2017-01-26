# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

ls = ['яблоко', 'банан', 'киви', 'арбуз', 'груша']
max_len = 0

for x in ls:
    if len(x) > max_len:
        max_len = len(x)

for i, s in enumerate(ls):
    print(i + 1, " " * (max_len - len(s)), s)


# Подсказка: использует метод .format()

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.
ls1 = [-1, 6, 7, -2, 23, 45, 11]
ls2 = [6, 3, -3, 45]

s1 = set(ls1)
s2 = set(ls2)
s3 = s1 - s2
print(list(s3))

# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

ls3 = [2, 3, 34, 5, 11, 7, 23, 28]
ls4 = []

for x in ls3:
    if x % 2 == 0:
        ls4.append(x >> 2)
    else:
        ls4.append(x << 1)

print(ls4)
