tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_tasks():
    new = input("Enter the task to append in To-Do list: ")
    tasks.append(new)
    print(f"Task '{new}' added.")

def mark_done():
    if not tasks:
        print("No tasks to mark as done.")
        return
    show_tasks()
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"'{removed}' was marked as Done and removed from the To-Do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n__To Do List__")
    print("1. View all tasks\n2. Add new task\n3. Mark task as done\n4. Quit")
    menu_choice = input("Please enter your choice: ")

    if menu_choice == "1":
        show_tasks()
    elif menu_choice == "2":
        add_tasks()
    elif menu_choice == "3":
        mark_done()
    elif menu_choice == "4":
        print("Thanks, have a good day ❤️")
        break
    else:
        print("Invalid choice T_T")
