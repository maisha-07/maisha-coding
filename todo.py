tasks = []

while True:
    print("1. Add task")
    print("2. Show all")
    print("3. Quit")
    choice = input("Choose: ")

    if choice == "1":
        # ask user for task and add to list
        task = input("Task? ")
        tasks.append(task)
        print("Added!")

    elif choice == "2":
        print("Your tasks:")
        for task in tasks:
            print(f"- {task}")
  
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice")
