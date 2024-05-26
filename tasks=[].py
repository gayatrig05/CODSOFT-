tasks=[]

def add_task():

    task=input("Enter a new task")
    tasks.append(task)
    print("Task has been added✅ to your directory")

def view_task():
    if len(tasks) == 0:
        print("There are no tasks in your Directory")
    else:
        print("These are your pending Tasks")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')

def delete_task():

    if len(tasks)==0:
        print("Your Directory is empty, there is nothing to be deleted")
    else:
        print('Tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        choice = int(input('Enter the Serial number of Task you want to Delete:'))

        if 0 < choice <=len(tasks):
            del tasks1[choice-1]
            print('Task has been removed✅')
        else:
            print('Invalid Serial Number')


def main():

    while True:
        print('\n /O\ /O\ To-Do-List CLI /O\ /O\ ')
        print('1. Add a Task')
        print('2. View Your Directory')
        print('3. Delete a Task')
        print('4. Exit')

        choice = int(input("Enter a Choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Exiting To-Do-List Application")
            break
        else:
            print('Invalid Choice please select an appropriate number')





if __name__ == "__main__":
    main()