#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
#монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
#количество монет, которые нужно перевернуть.

from random import randint

while True:
    count_coins = input("Введите количесво монет: ")
    if count_coins.isdigit():
        count_coins = int(count_coins)
        break
    else:
        print("Введите целое не отрицательное число")   

# count_heads - орел 1
# count_tails - решка 0

count_heads, count_tails = 0, 0

for _ in range(count_coins):
    now_coin = randint(0, 1)
    if(now_coin == 0):
        count_tails += 1
    else:
        count_heads += 1 

        count_day = 0

    print(now_coin, end=" ")          
    
print("") 
print(f"нужно перевернуть {min(count_tails, count_heads)} монет")