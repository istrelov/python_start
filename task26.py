# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии

def UserUnit(Message):
    while True:
        numbers = input(Message)
        if numbers.isdigit():
            numbers = int(numbers)
            break
        else:
            print("Введите целое не отрицательное число")   
    return numbers

def dev(number, index):
    if index == 1:
        return number
    return number * dev(number, index - 1)   


number_a = UserUnit("Введите число А: ")
number_b = UserUnit("Введите число B: ")

print(f"A = {number_a} B = {number_b} -> {dev(number_a, number_b)}")
