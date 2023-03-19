# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

while True:
    number_N = input("Введите число N: ")
    if number_N.isdigit():
        number_N = int(number_N)
        break
    else:
        print("Введите целое не отрицательное число")  

res, index = 2, 1
print(number_N, end=" -> ")

while res < number_N:
    print(res, end=" ")

    for _ in range(index):
        res*=2
    
