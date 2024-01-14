tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def list_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task description: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        task_index = int(input("Enter the task index to mark as completed: "))
        complete_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
