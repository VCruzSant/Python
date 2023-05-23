import os

list_task = []
task_deleted = []

def add_task(task, listta=None):
    listta.append(task)
    return listta

while True:
    print('comandos: listar, desfazer, refazer')
    command = input('Digite uma tarefa nova ou um comando: ')
    print()
    


    if command == 'listar':
        if list_task == []:
            print('sem nenhuma tarefa')
            print()
            continue
        
        print(list_task)
        print()
        continue


    elif command == 'desfazer':
        if list_task == []:
            print('nada para desfazer')
            print()
            continue
        
        last_task = list_task[-1]
        add_task(last_task, task_deleted)
        list_task.pop()
        print(list_task)
        print()
        continue


    elif command == 'refazer':
        if task_deleted == []:
            print('nada para refazer')
            print()
            continue
        
        last_task = task_deleted[-1]
        add_task(last_task, list_task)
        task_deleted.pop()
        print(list_task)
        print()
        continue

    elif command in ('1234567890'):
        print('número não é aceito')
        print()
        continue


    elif command == 'clear':
        os.system('cls')
        continue


    else:
        list_task.append(command)
        print(list_task)
        print()
        continue

    