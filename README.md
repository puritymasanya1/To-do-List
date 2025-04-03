# Simple To-Do List Application

A lightweight command-line to-do list manager built with Python that allows you to manage your daily tasks with ease.

## Features

- **Add Tasks**: Quickly add new tasks to your to-do list
- **View Tasks**: See all your current tasks with numbered entries
- **Remove Tasks**: Delete completed or unwanted tasks by their number
- **User-Friendly Interface**: Simple menu-driven experience

## Getting Started

### Prerequisites

- Python 3.x installed on your computer

### Running the Application

1. Save the code to a file named `todo_list.py`
2. Open a terminal or command prompt
3. Navigate to the directory containing the file
4. Run the program with:
   ```
   python todo_list.py
   ```

## How to Use

The application presents a simple menu with 4 options:

1. **Add Task**: Enter a description of your new task
2. **View Tasks**: Display all tasks in your to-do list with their numbers
3. **Remove Task**: Delete a task by entering its number
4. **Exit**: Close the application

### Example Usage

```
 TO-DO LIST MENU
1. Add task
2. View tasks
3. Remove task
4. Exit
Enter your choice: 1
Enter an new task: Buy groceries
Task 'Buy groceries' added to the list.

 TO-DO LIST MENU
1. Add task
2. View tasks
3. Remove task
4. Exit
Enter your choice: 2
To do list:
1. Buy groceries
```

## Code Structure

- `todolist`: A list that stores all task entries
- `my_menu()`: Displays the main menu options
- `add_task()`: Handles the logic for adding new tasks
- `view_task()`: Shows all current tasks with numbers
- `remove_task()`: Allows removal of tasks by number
- Main loop: Handles user input and function calls

