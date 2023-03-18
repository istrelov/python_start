#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
#билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером
#385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

def sum_numbers(number):
    numone = number // 100
    numsecond = number // 10 % 10
    numthird = number % 10
    return(numone + numsecond + numthird) 

ticket_number = int(input("Введите номер билета: "))

if sum_numbers(int(ticket_number / 1000)) == sum_numbers(ticket_number % 1000):
    print(f"{ticket_number} -> yes")
else:
    print(f"{ticket_number} -> no")
пше фвв