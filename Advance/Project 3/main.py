# do to list
#tasks = []
tasks = ["Buy milk", "Finish homework"]


def show_menu():
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove task")
    print("4. Exit")


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task: {task} ! added!")


def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nTasks")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("\n")    


def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Removed task: {removed}")
    except (ValueError, IndexError):
        print("Invalid choice!")


while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Enter valid option, Try again!!")
