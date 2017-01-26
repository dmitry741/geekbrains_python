# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    ''' функция возвращает ряд Фибоначчи с n-элемента до m-элемента.
    '''
    a1, a2 = 1, 1
    f = a1 + a2

    while f <= m:        
        if f >= n:
            print(f)

        a1 = a2
        a2 = f        
        f = a1 + a2

print("печатаем числа Фибоначчи:")
fibonacci(1, 100)
print("\n")
    

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def merge_sorted_array(A, B):
    ''' Сливание двух сортированных массивов в один
    '''
    iA, iB, iC = 0, 0, 0
    C = []

    while True:
        if iA == len(A):
            for b in range(iB, len(B)):
                C.append(B[b])
            break
        if iB == len(B):
            for a in range(iA, len(A)):
                C.append(A[a])
            break
       
        if A[iA] < B[iB]:
            C.append(A[iA])
            iA += 1
        else:
            C.append(B[iB])
            iB += 1

    return C

def sort_to_max(A):
    ''' сортировка массива методом quicksort
    '''
    if (len(A) < 2):
        return A;

    curList = []

    for a in A:
        ls = []
        ls.append(a)
        curList.append(ls)

    while len(curList) > 1:
        i = 0
        newList = []
        
        while i < len(curList) - 1:
            a1 = curList[i]
            a2 = curList[i + 1]
            res = merge_sorted_array(a1, a2)
            newList.append(res)
            i += 2

        if all([len(curList) % 2 == 1, len(curList) > 1]):
            a1 = newList.pop()
            a2 = curList[len(curList) - 1]
            res = merge_sorted_array(a1, a2)
            newList.append(res)

        curList = newList

    result = []
    result.extend(curList[0])
    
    return result;

sortedArray = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(sortedArray)

# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(f, ls):
    if not callable(f):
        return []
    
    result = []    

    for x in ls:
        if f(x):
            result.append(x)

    return result

ls = [2, 7, 9, 22, 17, 24, 8, 12, 27]
print(my_filter(lambda x: x % 2 == 0, ls))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4):

    def is_equal(x1, y1, x2, y2, x3, y3, x4, y4):
        l1 = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
        l2 = (x4 - x3) * (x4 - x3) + (y4 - y3) * (y4 - y3)
        return l1 == l2

    def is_collinear(x1, y1, x2, y2, x3, y3, x4, y4):
        ax = x2 - x1
        ay = y2 - y1
        bx = x4 - x3
        by = y4 - y3

        return (ax * by - bx * ay) == 0

    result = []

    result.append(is_equal(x1, y1, x2, y2, x3, y3, x4, y4))
    result.append(is_collinear(x1, y1, x2, y2, x3, y3, x4, y4))
    result.append(is_equal(x2, y2, x3, y3, x4, y4, x1, y1))
    result.append(is_collinear(x2, y2, x3, y3, x4, y4, x1, y1))

    return all(result)

print(is_parallelogram(0, 0, 1, 1, 3, 1, 2, 0))
print(is_parallelogram(0, 0, 0, 1, 1, 1, 1, 0))

