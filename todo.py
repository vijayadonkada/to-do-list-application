class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Invalid task index")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index + 1}. {task['task']} - {status}")


def main():
    task_manager = TaskManager()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            task_manager.add_task(task)
            print("Task added successfully")
        elif choice == "2":
            task_index = int(input("Enter the index of the task to mark as complete: ")) - 1
            task_manager.complete_task(task_index)
            print("Task marked as complete")
        elif choice == "3":
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            task_manager.remove_task(task_index)
            print("Task removed successfully")
        elif choice == "4":
            task_manager.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
