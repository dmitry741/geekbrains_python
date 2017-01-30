# my regex
import re

# 1. Сколько раз слово присутствует в строке
string = 'This is a simple test message for test'
found = re.findall(r'test', string)
print(found)

# 2. проверяем вхождение паттерна в конец строки
pattern1 = r'test$'
result = re.search(pattern1, string)
print(result)

# 3. проверяем вхождение паттерна в начало строки
pattern2 = r'^test'
result = re.search(pattern2, string)
print(result)

# 4. Найти все цифры в тексте
pattern3 = '\d+h'
string = 'If 300 spartans were so brave, so 500 spartans efe34h1trh'
print(re.findall(pattern3, string))
