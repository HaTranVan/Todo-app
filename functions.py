FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """read and get todo as a list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """write todos to a file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
