# Text-Based Note-Taking Application in Python

# Function to create a new note
def create_note():
    note_title = input("Enter the title of the note: ")
    note_content = input("Enter the content of the note: ")
    
    with open(f"{note_title}.txt", "w") as note_file:
        note_file.write(note_content)
    
    print(f"Note '{note_title}' created!")

# Function to view an existing note
def view_note():
    note_title = input("Enter the title of the note to view: ")
    
    try:
        with open(f"{note_title}.txt", "r") as note_file:
            note_content = note_file.read()
            print(f"Note: {note_content}")
    except FileNotFoundError:
        print(f"Note '{note_title}' not found.")

# Main program loop
while True:
    print("\nNote-Taking Menu:")
    print("1. Create a Note")
    print("2. View a Note")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        create_note()
    elif choice == '2':
        view_note()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
