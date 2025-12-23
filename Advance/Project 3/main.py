# do to list
tasks = []
def show_menu():
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove task")
    print("4. Exit")


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"TAsk {task} added!")


def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nTasks")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
