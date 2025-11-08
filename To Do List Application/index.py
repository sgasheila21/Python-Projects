import os
import platform

tasks = []


def clear_screen():
    system_name = platform.system()
    os.system("cls") if system_name == "Windows" else os.system("clear")


def menus():
    clear_screen()
    print("\n" + "=" * 30)
    print("To Do List".center(30))
    print("=" * 30)
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Show Tasks")
    print("5. Exit")


def show_tasks():
    max_task_length = max((len(task) for task in tasks), default=10)
    total_width = max_task_length + 6
    print("\nNo  | Task Name")
    print("-" * total_width)
    if not tasks:
        print("No task".center(total_width))
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i:<4}| {task}")


def get_task_number(action: str) -> int:
    if not tasks:
        print(f"\nNo tasks to {action}.")
        input("\nPress Enter to continue...")
        return None

    while True:
        try:
            task_number = int(input(f"Enter the task number to {action}: "))
            if 1 <= task_number <= len(tasks):
                return task_number
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


while True:
    menus()

    while True:
        choice = input("Select an option: ").strip()
        if choice in ['1', '2', '3', '4', '5']:
            break
        else:
            print("That’s not a valid option. Please choose 1, 2, 3, 4, or 5.")

    if choice == '1':
        while True:
            new_task = input("Enter new task: ").strip()
            if new_task == "":
                print("Task name cannot be empty or just spaces! Try again.")
            else:
                tasks.append(new_task)
                print(f"Task '{new_task}' added successfully.")
                break
        input("\nPress Enter to continue...")

    elif choice == '2':
        show_tasks()
        task_number = get_task_number("edit")
        if task_number:
            while True:
                new_task = input("Enter the new task name: ").strip()
                if new_task == "":
                    print("Task name cannot be empty or just spaces! Try again.")
                else:
                    old_task = tasks[task_number - 1]
                    tasks[task_number - 1] = new_task
                    print(f"Task '{old_task}' updated to '{new_task}'.")
                    break
            input("\nPress Enter to continue...")

    elif choice == '3':
        show_tasks()
        task_number = get_task_number("delete")
        if task_number:
            old_task = tasks.pop(task_number - 1)
            print(f"Task '{old_task}' deleted successfully.")
            input("\nPress Enter to continue...")

    elif choice == '4':
        show_tasks()
        input("\nPress Enter to continue...")

    elif choice == '5':
        print("Goodbye")
        break
