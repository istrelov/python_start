#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N 
# – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

def UserUnit(Message):
    while True:
        numbers = input(Message)
        if numbers.isdigit():
            numbers = int(numbers)
            break
        else:
            print("Введите целое не отрицательное число")   
    return numbers

from random import randint

count_list = UserUnit("Введите количество элементов: ")
find_number = UserUnit("Введите искомое число: ")

my_list = [randint(1, 10) for i in range(count_list)]
print(my_list)

count_num = 0
min_dif = 99
similar_num = 0

for i in my_list:
    if i == find_number:
        count_num += 1
    else:
        if abs(i -find_number) < min_dif:
           min_dif = abs(i -find_number)
           similar_num = i

if count_num > 0:
    print(f"число встречается {count_num} раз")
else:
    print(f"самое близкое число {similar_num}")
