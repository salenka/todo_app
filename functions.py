
def get_todos(filepath=r"todos.txt"):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """Grava a tarefa"""
    with open(filepath, "w") as file2:
        file2.writelines(todos_arg)


if __name__ == "__main__":
    print ("hello from functions")
# print(__name__)