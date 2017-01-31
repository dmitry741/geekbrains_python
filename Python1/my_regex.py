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
pattern3 = '[1-9]+'
string = 'If 300 spartans were so brave, so 500 spartans efe34h1trh'
print(re.findall(pattern3, string))

# 5. Задание-1 из домашней работы урок 4
# Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp'
pattern5 = '[a-z]+'
print(re.findall(pattern5, line))

# 6. 
pattern6 = r'[A-Z]{,2}\s'
line = 'sGAMkgAYE OmHBSQsasd'
print(line)
print(re.findall(pattern6, line))
      
# 7. 
pattern7 = r'\w+\.{,1}\w+@\w+\.\w{2,3}'
line = 'dmitrypavlov74@gmail.com fewgfuwg few 321476gfwf \ndmitry.pavlov2012@yandex.ru ssuloev@gmail.com werwer'
print('line = ', line)
print(re.findall(pattern7, line))
