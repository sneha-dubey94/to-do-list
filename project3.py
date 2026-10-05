 Simple To-Do List

t#asks = []

while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Remove task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task removed successfully!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice!")