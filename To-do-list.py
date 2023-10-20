# To-Do List Application in Python

# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)  # Add the entered task to the tasks list
    print("Task added!")

# Function to display all tasks
def display_tasks():
    if not tasks:  # Check if the tasks list is empty
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):  # Enumerate and display each task with a number
            print(f"{i}. {task}")

# Function to remove a task
def remove_task():
    display_tasks()  # Display the list of tasks before removal
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):  # Check if the entered task number is valid
            removed_task = tasks.pop(task_number - 1)  # Remove the task at the specified index
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Enter a task number.")

# Main program loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
