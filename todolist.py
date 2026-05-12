def show_menu():
    print("\n" + "="*30)
    print("      TO-DO LIST APP")
    print("="*30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("="*30)


def add_task():
    task = input("Enter your task: ")

    with open("tasks.txt", "a") as file:
        file.write(task + " | Pending\n")

    print("✔ Task added successfully!")


def view_tasks():
    print("\n--- YOUR TASKS ---")

    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            if not tasks:
                print("No tasks found!")
                return

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

    except FileNotFoundError:
        print("No tasks found!")


def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to delete!")
            return

        print("\n--- YOUR TASKS ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        task_num = int(input("Enter task number to delete: "))

        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number!")
            return

        removed = tasks.pop(task_num - 1)

        with open("tasks.txt", "w") as file:
            file.writelines(tasks)

        print(f"✔ Deleted: {removed.strip()}")

    except ValueError:
        print("Please enter a valid number!")

    except FileNotFoundError:
        print("No tasks file found!")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("Exiting... Goodbye 👋")
            break

        else:
            print("Invalid choice! Try again.")


main()