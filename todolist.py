import functions
import time

now_time = time.strftime("%b %d, %Y  %H:%M:%S")
print(now_time)

file_path = 'todos.txt'

while True:
    user_action = input('Add, show, edit, complete or exit: ').strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos(file_path)

        todos.append(todo)

        functions.write_todos(file_path, todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos(file_path)

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f'{index + 1}. {todo}')

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos(file_path)

            index_edit = int(user_action[5:])
            edit_todo = input('New todo: ')
            todos[index_edit - 1] = edit_todo + '\n'

            functions.write_todos(file_path, todos)

        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos(file_path)

            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            message = f"Todo: {todo_to_remove} was removed from the list"
            print(message)

            functions.write_todos(file_path, todos)

        except IndexError:
            print('There is no item with that number.')
            continue
        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print('See u soon.')
