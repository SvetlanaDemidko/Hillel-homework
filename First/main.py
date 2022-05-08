# Task 1.1 убрать из массива повторяющиеся элементы

a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
print(list(set(a)))

# Task 1.2 вывести 3 наибольших числа из исходного массива
lst = [9,7,43,2,4,7,8,9,4]
ranks = sorted( [(x,i) for (i,x) in enumerate(a)], reverse=True )
box = []
for x,i in ranks:
    if i&x not in box:
        box.append( x )
        if len(box) == 3:
            break
print(box)

# Task 1.3 вывести индекс минимального элемента массива
minNum = min(a)
print(a.index(minNum))

# Task 1.4  вывести исходный массив в обратном порядке
print(list(reversed(a)))

# Task 2 Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
def createList(r1, r2):
    if (r1 == r2):
        return r1
    else:
        res = []
        while(r1 < r2+1):
            res.append(r1)
            r1 += 1
        print(res)
    for ev in res:
        if (ev % 2 != 0):
            res.remove(ev)
    return res
# Driver Code
r1, r2 = 0, 100
print(createList(r1, r2))

# Task 3 Найти общие ключи в двух словарях:

dict_one = {'a':'1', 'b':'2', 'c':'3',  'd':'4'}
dict_two = {'a':'6', 'b':'7', 'z':'20', 'x':'40'}
arr = []
for key in dict_one.keys():
    if key in dict_two.keys():
        arr.append(key)

print(arr)


# Task 4 Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
# keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ожидаемый результат: {1: 1, 2: 4, 3: 9 …}

a = {a : a ** 2 for a in range (10)}
a.pop(0)
print(a)

