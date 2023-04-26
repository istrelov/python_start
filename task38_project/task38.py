# Задача 38 Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
#1. Программа должна выводить данные
#2. Программа должна сохранять данные в текстовом файле
#3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
#4. Использование функций. Ваша программа не должна быть линейной
#5 Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

def UserUnit(Message):
    while True:
        numbers = input(Message)
        if numbers.isdigit:
            numbers = int(numbers)
            break
        else:
            print("Введите целое не отрицательное число не больше 6")   
    return numbers

def read_file():
    file = open('phonebook.txt', 'r', encoding = 'UTF-8')
    data = file.readlines()
    file.close() 

    return data

def create_phone_dictionary():
    data = read_file()
    phone_book = []
    
    for contact in data:
        new_contact = contact.strip().split(';')
        new_contact = {'name': new_contact[0], 'surname': new_contact[1], 'secondname': new_contact[2], 'phone': new_contact[3]}
        phone_book.append(new_contact)

    return phone_book

def print_phone():
    data = read_file()

    for contact in data:
        print(contact)

def add_contact():
    name = input('Фамилия: ')   
    surname = input('Имя: ') 
    secondname = input('Отчество: ')
    phone = input('Номер телефона: ') 
     
    new_data = '\n' + name + ';' + surname + ';' + secondname + ';' + phone
    
    file = open('phonebook.txt', 'a', encoding = 'UTF-8') 
    file.write(new_data)
    file.close()

def map_property(number_property):
    if number_property == 1:
        property_name = 'name'
    elif number_property == 2:
        property_name = 'surname'
    elif number_property == 3:
        property_name = 'secondname'
    elif number_property == 4:
        property_name = 'phone'

    return property_name  

def find_contact(phone_book, need_print):
    seach_property = UserUnit('Свойство поиска (1 - фамилия, 2 - имя, 3 - отчество, 4 - телефон):')
    seach_value = input('Что искать:')

    findindex = -1
    seached = False

    for person in phone_book:
        findindex += 1

        if person[map_property(seach_property)].lower() == seach_value.lower():
            if need_print:
                print(' '.join([values for values in person.values()]))
            seached = True
            break
    
    if seached == False:
        findindex = -1

    return findindex

def find_watch_contact():
    phone_book = create_phone_dictionary()
    findindex = find_contact(phone_book, True)

    if findindex == -1:
        print('Контакт не был найден')    

def print_menu():
    print('Меню телефонного справочника:')
    print(' 1 - прочитать справочник;')
    print(' 2 - добавить;')
    print(' 3 - найти;')
    print(' 4 - удалить запись;')
    print(' 5 - изменить запись;')
    print(' 6 - показать меню;')
    print(' 7 - закрыть программу;')

def delete_contact():
    phone_book = create_phone_dictionary()
    findindex = find_contact(phone_book, False)

    if findindex == -1:
        print('Контакт не был найден')  
        return
    
    del_value = phone_book.pop(findindex)
    save_file(phone_book)

def edit_contact():
    phone_book = create_phone_dictionary()
    findindex = find_contact(phone_book, True)

    if findindex == -1:
        print('Контакт не был найден')  
        return
    
    edit_property = UserUnit('Какое свойство поменять (1 - фамилия, 2 - имя, 3 - отчество, 4 - телефон):')
    new_value = input('Новое значение: ')

    phone_book[findindex][map_property(edit_property)] = new_value
    save_file(phone_book)

def execute_user_comand(comand):
    if comand == 1:
        print_phone()
    elif comand == 2:
        add_contact()        
    elif comand == 3:
        find_watch_contact()
    elif comand == 4:
        delete_contact()       
    elif comand == 5:
        edit_contact()       
    elif comand == 6:
        print_menu()

def save_file(phone_book):
    new_phone_book = []

    for contact in phone_book:
        new_contact = ';'.join([values for values in contact.values()])
        new_phone_book.append(new_contact)  
    
    new_phone_book = '\n'.join(new_phone_book)

    file = open('phonebook.txt', 'w', encoding = 'UTF-8')
    file.write(new_phone_book)
    file.close()

# основной блок программы
user_comand = 6
while user_comand < 7:
    execute_user_comand(user_comand)
    user_comand = UserUnit('Введи действие: ')

print('работа программы завершена')





    


    

