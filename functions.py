from const import *

def add_user ():
    while True:
        a = input ('Введите имя\n')
        if a == '0':
            break
        else:
            name_list = DICT.get('name')
            name_list.append(a)
            DICT.update (name = name_list)
            b = int (input ('Введите возраст\n'))
            age_list = DICT.get ('age')
            age_list.append (b)
            DICT.update (age = age_list)
            c = input ('Введите пол\n')
            gender_list = DICT.get ('gender')
            gender_list.append (c)
            DICT.update (gender = gender_list)
    print (DICT)
add_user()

def show_user ():
    a = int(input('Введите индекс пользователя, чьи данные необходимо показать\n'))
    a_list = DICT.get ('name')
    b_list = DICT.get ('age')
    c_list = DICT.get ('gender')
    print (a_list[a-1], b_list[a-1], c_list[a-1])

show_user()

def num_user ():
    b = input ('Введите имя пользователя, чьи данные хотите посмотреть\n')
    b_list = DICT.get ('name')
    a_list = DICT.get ('age')
    c_list = DICT.get ('gender')
    if b in b_list:
        a = b_list.index(b)
        print (b_list[a], a_list [a], c_list[a])
num_user()

def del_user ():
    x = int(input('Введите индекс пользователя, чьи данные надо удалить\n'))
    x_list = DICT.get ('name')
    x_list.pop (x-1)
    DICT.update (name = x_list)
    x_list = DICT.get('age')
    x_list.pop(x - 1)
    DICT.update(age=x_list)
    x_list = DICT.get('gender')
    x_list.pop(x - 1)
    DICT.update(gender=x_list)

del_user()

print (DICT)