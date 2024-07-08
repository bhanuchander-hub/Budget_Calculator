# budget1.py
python code for budget tracker
import json
from datetime import datetime

# Load tasks from a file
def load_tasks(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to a file
def save_tasks(tasks, file_path):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    name = input("Enter task name: ")
    priority = input("Enter task priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"name": name, "priority": priority, "due_date": due_date, "completed": False})

# Remove a task
def remove_task(tasks):
    task_index = int(input("Enter the index of the task to remove: "))
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid index")

# Mark a task as completed
def complete_task(tasks):
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
    else:
        print("Invalid index")

# Display all tasks
def display_tasks(tasks):
    for index, task in enumerate(tasks):
        completed = "X" if task["completed"] else " "
        print(f"{index}: [{completed}] {task['name']} (Priority: {task['priority']}, Due Date: {task['due_date']})")

def main():
    file_path = "tasks.json"
    tasks = load_tasks(file_path)

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks, file_path)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
