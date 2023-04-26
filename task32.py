# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def UserUnit(Message):
    while True:
        numbers = input(Message)
        if numbers.isdigit():
            numbers = int(numbers)
            break
        else:
            print("Введите целое не отрицательное число")   
    return numbers

def gen_list(count_list, max_item):
    list_random = [randint(1, max_item + 10) for _ in range(count_list)]
    print(list_random)
    return list_random

count = UserUnit("Введите количество элементов: ")
min_item = UserUnit("Введите минимальное значение: ")
max_item = UserUnit("Введите максимальное значение: ")

list_random = gen_list(count, max_item)
res_list = []

for index in range(count):
    if min_item < list_random[index] < max_item:
        res_list.append(index) 

print(res_list)
