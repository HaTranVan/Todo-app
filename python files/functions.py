def get_todos(filepath):
    """read and get todo as a list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    """write todos to a file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
