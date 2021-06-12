from random import choice
#import random
# Запрашивать у пользователя команду.
# В зависимости от введенной команды выполнять действия.
HELP = """
* help - напечатать справку по программе.
* add - добавить задачу в список (название задачизапрашиваему пользователя).
* show - напечатать все добавленные задачи во все дни (сегодня, завтра, другое).
* q - выход из программы.
* random - добавить случайную задачу на сегодня
"""
RANDOM_TASK = [
    'Написать Гвидо письмо',
    'Выучить Python',
    'Записаться на курс в Нетологию',
    'Посмотреть 4 сезон Рик и Морти'
]
todo = {}
flag = True

def add_todo(day,task):
    if day not in todo:
        todo[day] = []
    todo[day].append(task)
    print(f"Задача {task} добавлена на дату {day}")

while flag:
    command = input("Введите команду: \n")

    if command == "help":
        print(HELP)
    elif command == "add":
        day = input("Введите дату: ")
        task = input("Введите задачу: ")
        add_todo(day,task)

    elif command == "show":
        day = input("Введите дату: ")
        if day in todo:
            for task in todo[day]:
                print(f'[] {task}')
        else:
            print(f"Задач на эту дату нет!")
    elif command == "random":
        day = 'сегодня'
        add_todo(day, choice(RANDOM_TASK))
        # add_todo(day, random.choice(RANDOM_TASK))

    elif command == "q":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда!")