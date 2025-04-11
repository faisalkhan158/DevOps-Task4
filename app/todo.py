import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("[📭] No tasks yet.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("[➕] Task added.")

def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"[🗑️] Task '{removed}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def mark_task_done():
    tasks = load_tasks()
    view_tasks()
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index] += " ✅"
            save_tasks(tasks)
            print("[✅] Task marked as done.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def clear_tasks():
    save_tasks([])
    print("[🧹] All tasks cleared.")

def menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as done")
        print("5. Exit")
        print("6. Clear all tasks")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_done()
        elif choice == "5":
            print("👋 Exiting. Goodbye!")
            break
        elif choice == "6":
            clear_tasks()
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
