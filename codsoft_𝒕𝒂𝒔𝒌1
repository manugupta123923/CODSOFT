# TO-DO LIST

Activity = []

while True:
    print("\n1. Add Activity\n2. Observe Activity\n3. Remove Activity\n4. Exit")
    selection = input("select an option: ")

    if selection == "1":
        
        task = input("Enter a task: ")
        Activity.append(task)
        print("Activity added!")

    elif selection == "2":
        if Activity:
            print("\nYour To-Do List:")
            index = 1  # Manual index
            for task in Activity:
                print(f"{index}. {task}")  
                index += 1  
        else:
            print("No Activity yet!")

    elif selection == "3":
        if Activity:
            index = 1 
            for task in Activity:  
                print(f"{index}. {task}")  
                index += 1

          
                Activity_num = int(input("Enter Activity number to remove: "))
                if 1 <= Activity_num <= len(Activity): 
                    
                    removed_activity = Activity.pop(Activity_num - 1)

                    print(f"Activity '{removed_activity}' removed!")
                else:
                    print("Invalid number!")
            
        else:
            print("No Activity to remove!")

    elif selection == "4":
        print("bye!")
        break

    else:
        print("Invalid selection! Try again.")  
