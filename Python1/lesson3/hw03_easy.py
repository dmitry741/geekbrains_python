# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math


def my_round(number, ndigits):
    ''' Функция округляет полученное произвольное десятичное число
    до опредеяемого вторым параметром кол-ва знаков
    '''    
    s = str(number)
    ls = s.split('.')

    if len(ls) < 2:  # перед нами целое число
        return number    

    head = int(ls[0])  # целая часть
    tail = ls[1]  # дробная часть как целое число

    if len(tail) <= ndigits:  # число и так содержит не больше знаков после запятой чем требуется
        return number
    
    last_digit = tail[ndigits:ndigits + 1]

    if ndigits > 0:
        short_tail = tail[:ndigits]
        result = head + float(short_tail) / 10 ** len(short_tail)
    else:
        result = head

    if int(last_digit) >= 5:
        a = 1 / 10 ** ndigits
        result += a

    if type(result) == float:
        if float.is_integer(result):
            result = int(result)

    return result
    

help(my_round)
print("результат округления = ", my_round(12.1234567, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ''' функция определяет является ли билет счастливым или нет
    '''
    a, b, r = 0, 0, 0
    n = ticket_number

    for x in range(6):
        r = n % 10
        
        if x < 3:
            a += r            
        else:
            b += r

        n = int((n - r) / 10)

    return a == b

help(lucky_ticket)
print(lucky_ticket(333351))
