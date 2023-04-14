#Задача36 Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
#вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
#Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
#как, например, у операции умножения

def print_operation_table(operation, num_rows=6, num_columns=6):
    
    #new_list = list(map(print_one, range(1, num_rows+1), operation, num_columns))
    #print(new_list)
    #print(operation())
    #new_list_2 = list(map(lambda y: y, range(1, num_rows+1)))
    #print(new_list_2)

    #print(operation(2, 3))
    #operation(new_list, new_list_2)
   for i in range(num_rows):
        for j in range(num_columns):
            print(operation(i+1, j+1), end = " ")  
        print("")  

print_operation_table(lambda x, y: x * y, 6, 6)