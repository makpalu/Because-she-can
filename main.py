from todolistBSC import Todo, Todolist

# # todo_name = input("Enter a todo: ")
# todo1 = Todo(todo_name, 1, 1, 20, False, True)
# todolist1 = Todolist("School work", "For keeping school stuff")
# for i in range(1, 6):
#     todolist1.add_todo(Todo(input(f"Enter todo {i}"), i, i, 23, False, True))
# todolist1.add_todo(todo1)
# print(todolist1.get_todo_names())

#Write a program that allows you to create multiple todolist and multiple todos and be able to store the todos and the todolist

is_running = True
todolists = []

while is_running:
    print("Enter 1 to create a todolist")
    print("Enter 2 to create a todo")
    print("Enter 3 to quit")
    x = input("x: ")
    if x == "1":
        todolist = Todolist(input("Enter the name of the todolist: "), input("Enter the description: "))
        todolists.append(todolist)
    elif x == "2":
        if not todolists:
            print("Todolist not available. Create one first.")
            continue
        print("Select the todolist to add it to: ")
        for index, element in enumerate(todolists, 1):
            print(f"{index}. {element.get_name()}")

        user_input = 0

        while user_input < 1 or user_input > len(todolists):
            user_input = int(input(("Enter your option: ")))
        selected_todolist = todolists[user_input - 1]
        
        todo_name = input("Enter your task: ")
        todo_id = input("Enter the id: ")
        todo_level = input("Enter the priority level: ")
        todo_deadline = input("Enter the deadline: ")
        todo = Todo(todo_name, todo_id, todo_level, todo_deadline, False, True)
        selected_todolist.add_todo(todo)
    elif x == "3":
        is_running = False
    else:
        print("Enter a valid input.")
        