# coding: utf8
import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# и второй скрипт удаляющий эти папки

# cоздаем директории
for p in range(1, 10):
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(p))
    print(dir_path)
    
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
        break

# удаляем директории
for p in range(1, 10):
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(p))
    print(dir_path)
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Директория не существует')
        break

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
list_dir = os.listdir(os.getcwd())
print(list_dir)

for p in list_dir:
    if os.path.isdir(p):
        print(p)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

s = ''

with open('hw05_easy.py', 'r') as fr:
    for line in fr:
        s = ''.join([s, str(line)])

with open('hw05_easy_copy.py', 'w') as fw:
    fw.write(s)
