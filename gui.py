import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme('Black')

clock = sg.Text(key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(key='Add', size=4, image_source='add.png',
                       mouseover_colors='LightBlue2', tooltip='Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 7))
edit_button = sg.Button('Edit', size=(4, 1))
complete_button = sg.Button(key='Complete', size=4, image_source='complete.png',
                            mouseover_colors='LightBlue2', tooltip='Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My to-do App',
                   layout=[[clock],
                           [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Arial', 16))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case 'Add':
            todos = functions.get_todos()
            # reject empty todo and white space todo
            if not values['todo'] or values['todo'].isspace():
                sg.popup('Please type todo')
            else:
                todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                new_todo = values['todo'] + '\n'
                todo_to_edit = values['todos'][0]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select item first', font=('Ariel', 16))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_remove = values['todos'][0]

                todos = functions.get_todos()
                todos.remove(todo_to_remove)

                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select item first', font=('Ariel', 16))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
