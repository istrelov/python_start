#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
#Помогите Кате отгадать задуманные Петей числа.

def UserUnit(Message):
    while True:
        numbers = input(Message)
        if numbers.isdigit():
            numbers = int(numbers)
            break
        else:
            print("Введите целое не отрицательное число")   
    return numbers

sum_numbers = UserUnit("Введите сумму числел: ")
product_numbers = UserUnit("Введите произведение числел: ")

number_X = 1
find_over = False

while number_X < (sum_numbers - 1):
    number_Y = 1
    while number_Y <= (sum_numbers - number_X):
        if (number_X + number_Y == sum_numbers) and (number_X * number_Y == product_numbers):
            find_over = True
            break;

        number_Y+=1
    
    if find_over:
        break
    else:
        number_X +=1

if find_over:
    print(f"X = {number_X}, Y = {number_Y}") 
else:
    print(f"нет таких чисел")  