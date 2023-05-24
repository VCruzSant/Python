import os
import json


def read_task(task, path):
    data = []
    try:
        with open(path, "r", encoding="utf8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("arquivo não existe")
        save_task(task, path)
    return data


def save_task(task, path):
    data = []
    with open(path, "w", encoding="utf8") as file:
        data = json.dump(task, file, indent=2, ensure_ascii=False)
    return data


def add_task(task, listta=None):
    listta.append(task)
    return listta


PATH_FILE = "task_list.json"
list_task = read_task([], PATH_FILE)
task_deleted = []


while True:
    print("comandos: listar, desfazer, refazer")
    command = input("Digite uma tarefa nova ou um comando: ")
    print()

    if command == "listar":
        if list_task == []:
            print("sem nenhuma tarefa")
            print()
            continue

        print(list_task)
        print()
        continue

    elif command == "desfazer":
        if list_task == []:
            print("nada para desfazer")
            print()
            continue

        last_task = list_task[-1]
        add_task(last_task, task_deleted)
        list_task.pop()
        save_task(list_task, PATH_FILE)
        print(list_task)
        print()
        continue

    elif command == "refazer":
        if task_deleted == []:
            print("nada para refazer")
            print()
            continue

        last_task = task_deleted[-1]
        add_task(last_task, list_task)
        task_deleted.pop()
        save_task(list_task, PATH_FILE)
        print(list_task)
        print()
        continue

    elif command in ("1234567890"):
        print("número não é aceito")
        print()
        continue

    elif command == "clear":
        os.system("cls")
        continue

    list_task.append(command)
    print(list_task)
    print()
    save_task(list_task, PATH_FILE)
    continue
