Activity = []

while True:
    print("\n1. Add Activity\n2. Observe Activity\n3. Remove Activity\n4. Exit")
    selection = input("select an option: ")

    if selection == "1":
        
        task = input("Enter a task: ")
        Activity.append(task)
        print("Activity added!")

    elif selection == "2":
        if Activity :
            print("\nYour To-Do List:")
            index = 1  # Manual index
            for task in Activity:
                print(f"{index}.{Activity}")
                index += 1  # Increment index manually
        else:
            print("No Activity yet!")

    elif selection == "3":
        if Activity:
            index = 1  # Manual index
            for Activity in Activity:
                print(f"{index}. {Activity}")
                index += 1

            Activity_num = int(input("Enter Activity number to remove: "))
            if 1 <=Activity_num <= len(Activity):
                Activity.pop(Activity_num - 1)
                print("Activity removed!")
            else:
                print("Invalid number!")
        else:
            print("No Activity to remove!")

    elif selection == "4":
        print("bye!")
        break

    else:
        print("Invalid selection! Tryagain.")
