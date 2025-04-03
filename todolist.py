todolist = []

def my_menu(): 
    print("\n TO-DO LIST MENU") #prints a new line and the menu title
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def add_task():
    task = input("Enter an new task: ")  
    todolist.append(task)  
    print(f"Task '{task}' added to the list.")

def view_task():
    if not todolist:
        print("No tasks in the list.")
    else:
        print("To do list:")
        for index, task in enumerate(todolist, start=1):  # start=1 to number the tasks from 1
            print(f"{index}. {task}")

def remove_task():
    view_task()  # Display tasks before removing
    if todolist:
        try:
            task_number = int(input("Enter the task number to remove: "))  
            if 1 <= task_number <= len(todolist):
                removed_task = todolist.pop(task_number - 1)  # Remove the task from the list
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
while True:
    my_menu()
    choice = input("Enter your choice: ")  # Get user input
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting To do List. Ciao!")
        break
    else:
        print("Invalid choice. Enter a number between 1 and 4")

