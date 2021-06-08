# Запрашивать у пользователя команду.
# В зависимости от введенной команды выполнять действия.
HELP = """
* help - напечатать справку по программе.
* add - добавить задачу в список (название задачизапрашиваему пользователя).
* show - напечатать все добавленные задачи.
"""
tasks = []

while True:
    command = input("\nВведите команду: ")
    if command == "help":
        print(HELP)
    elif command == "add":
        task = input("Введите задачу: ")
        tasks.append(task)
        print("Задача добавлена")
    elif command == "show":
        print(tasks)
    else:
        print("Неизвестная команда!")