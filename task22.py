#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

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

count_list1 = UserUnit("Введите количество элементов множества 1: ")
count_list2 = UserUnit("Введите количество элементов множества 2: ")

my_list1 = [randint(1, 100) for i in range(count_list1)]
print(my_list1)

my_list2 = [randint(1, 100) for i in range(count_list2)]
print(my_list2)

set_my_list1 = set(my_list1)
set_my_list2 = set(my_list2)

inset = set_my_list1.intersection(set_my_list2)
print(inset)