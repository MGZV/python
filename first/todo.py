# Запрашивать у пользователя команду.
# В зависимости от введенной команды выполнять действия.
HELP = """
* help - напечатать справку по программе.
* add - добавить задачу в список (название задачизапрашиваему пользователя).
* show - напечатать все добавленные задачи во все дни (сегодня, завтра, другое).
* q - выход из программы.
"""
today = []
tomorrow = []
other = []
flag = True
while flag:
    command = input("Введите команду: \n")

    if command == "help":
        print(HELP)
    elif command == "add":
        day = input("Введите дату: ")
        task = input("Введите задачу: ")

        if day == "Сегодня":
            today.append(task)
        elif day == "Завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print(f"Задача {task} добавлена")


    elif command == "show":
        print("Сегодня")
        for task in today:
            print(task)
        print("Завтра")
        for task in tomorrow:
            print(task)
        print("Другие")
        for task in other:
            print(task)

    elif command == "q":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда!")