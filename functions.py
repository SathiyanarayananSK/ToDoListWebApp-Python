FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read the file and return the list of to-dos
    """
    with open(filepath, "r") as text_file:
        todos_content = text_file.readlines()
        return todos_content

def write_todos(todos_local, filename=FILEPATH):
    """
    Write the to-do items in the text file
    """
    with open(filename, "w") as text_file:
        text_file.writelines(todos_local)


if __name__ == "__main__":
    print(get_todos())