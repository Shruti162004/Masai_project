class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def delete_task(self, task_number):
        try:
            task_number = int(task_number)
            if task_number < 1 or task_number > len(self.tasks):
                raise ValueError
            task = self.tasks.pop(task_number - 1)
            print(f"Task '{task}' deleted successfully.")
        except ValueError:
            print("Invalid task number. Please enter a valid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def run(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. Add task")
            print("2. Delete task")
            print("3. View tasks")
            print("4. Quit")
            choice = input("Choose an option: ")
            if choice == "1":
                task = input("Enter the task to add: ")
                self.add_task(task)
            elif choice == "2":
                if not self.tasks:
                    print("No tasks available to delete.")
                else:
                    self.view_tasks()
                    task_number = input("Enter the task number to delete: ")
                    self.delete_task(task_number)
            elif choice == "3":
                self.view_tasks()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
