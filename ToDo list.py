#ToDo List
import json
import os

class ToDo_list:
    def __init__(self,file_name='todo_list.json'):
        self.file_name=file_name
        self.tasks=self.load_tasks()
    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name,'r') as file:
                return json.load(file)
        else:
            return []    
        
    def save_tasks(self):
        with open(self.file_name,'w') as file:
            json.dump(self.tasks,file,indent=4)
    def add_task(self,task):
        self.tasks.append({'task':task,'done':False})
        self.save_tasks()
        print(f"Task added:{task}")
    def update_task(self,index,new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task']=new_task
            self.save_tasks()
            print(f"Updated task {index} to :{new_task}")
        else:
            print(f"Task{index} does not exist.")
    def delete_task(self,index):
        if 0 <= index < len(self.tasks):
            task=self.tasks.pop(index)
            self.save_tasks()
            print(f"Deleted Task: {task['task']}")
        else:
            print(f"Tas{index} does not exist")
    def mark_as_done(self,index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done']=True
            self.save_tasks()
            print(f"Marked task {index} as done")
        else:
            print(f"task {index} does not exist.")
    def view_tasks(self):
        if not self.tasks:
            print("No Tasks in the list")
        else:
            for i,task in enumerate(self.tasks):
                status='done' if task['done'] else 'Not done'
                print(f"{i}:{task['task']}[{status}]")
def main():
    todo_list=ToDo_list()


    while True:
        print("\nToDo list options:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3.Update Task")
        print("4.Delete Task")
        print("5.Mark Task as Done")
        print("6.Exit")
        choice=input("Choose an option:")


        if choice =='1':
            todo_list.view_tasks()
        elif choice =='2':
            task=input("Enter the task:")
            todo_list.add_task(task)
        elif choice =='3':
            index=int(input("Enter the task index to update:"))
            new_task=input("Enter the New task:")
            todo_list.update_task(index,new_task)
        elif choice =='4':
            index=int(input("Enter the task index to delete:"))
            todo_list.delete_task(index)
        elif choice =='5':
            index=int(input("Enter the task index to mark as done:"))
            todo_list.mark_as_done(index)
        elif choice =='6':
            break
        else:
            print("Invalid choice.. Try Again...")
if __name__=='__main__':
    main()
        