# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических 
#операций допускаются только +1 и -1. Также нельзя использовать циклы.

def UserUnit(Message):
    while True:
        numbers = input(Message)
        if numbers.isdigit():
            numbers = int(numbers)
            break
        else:
            print("Введите целое не отрицательное число")   
    return numbers

def simple_sum(number, index):
    if index == 0:
        return number
    return simple_sum(number + 1, index - 1)   


number_a = UserUnit("Введите число А: ")
number_b = UserUnit("Введите число B: ")

print(f"A = {number_a} B = {number_b} -> {simple_sum(number_a, number_b)}")