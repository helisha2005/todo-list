
tasks = []

while True:
    print("\nSimple To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        task = input("What's the task? ")
        tasks.append(task)
        print(f'Added: "{task}"')
    
    elif choice == "2":
        if not tasks:
            print("Your list is empty!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    
    elif choice == "3":
        if not tasks:
            print("No tasks to delete!")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            task_num = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                removed = tasks.pop(task_num)
                print(f'Removed: "{removed}"')
            else:
                print("Invalid task number!")
    
    elif choice == "4":
        print("\nGoodbye!")
        break
    
    else:
        print("\nInvalid choice. Please enter 1-4.")