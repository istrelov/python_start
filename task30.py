#Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры

def UserUnit(Message):
    while True:
        numbers = input(Message)
        if numbers.isdigit():
            numbers = int(numbers)
            break
        else:
            print("Введите целое не отрицательное число")   
    return numbers

first_item = UserUnit("Введите первый элемент: ")
different = UserUnit("Введите разность: ")
count = UserUnit("Введите количество: ")

res_list = [first_item]

while count > 1:
    first_item += different
    res_list.append(first_item) 
    count -= 1

print(res_list)