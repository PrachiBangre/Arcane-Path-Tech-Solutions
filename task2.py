#TO-DO LIST

To_Do_List =[] #to-do list ,intially empty

#to view to-do list
def task_view():
    if To_Do_List:
        print('To-Do List : ')
        for i, task in enumerate(To_Do_List,start=1):
            print(f"{i}.{task}")
    else:
        print("Your To-Do List is empty")

#to add task in to-do list
def task_add():
    To_Do_List.append(task)
    print(f"Added Task :{task}")

# to delete task from to-do list
def task_delete(index):
    if index>=0 and index < len(To_Do_List):
        deleted_task = To_Do_List.pop(index)
        print(f"Task deleted : {task_delete}")
    else:
        print("Entered Task Index Is Invalid !")

# for calling function repetedly
while True:
    print('\nChoices')
    print('1 - View Task')
    print('2 - Add Task')
    print('3 - Delete Task')
    print('4 - Exit')

    choice=input('Enter Your Choice - ')

    if choice=="1":
        task_view()
    elif choice=="2":
        task=input('Enter Task - ')
        task_add()
    elif choice=="3":
        index=int(input('Enter Task number to delete - '))
        task_delete(index)
    elif choice=="4":
        break
    else:
        print("Invalid Choice.Try Again.")

