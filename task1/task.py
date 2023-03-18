#Задача 2: Найдите сумму цифр трехзначного числа. 

number = int(input("Введите трехзначное число: "))

numone = number // 100
numsecond = number // 10 % 10
numthird = number % 10

sumnumber = numone + numsecond + numthird 

print(f"{number} -> {sumnumber} ({numone} + {numsecond} + {numthird})")