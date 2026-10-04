# 14th github project --> Daily Habit Tracker
print("----------Daily Habit Tracker----------")

habits = []

while True:
    print("\n--- Habit Tracker ---")
    print("1. Add habit")
    print("2. View habits")
    print("3. Mark done")
    print("4. Quit")

    choice = input("Pick 1-4: ")

    if choice == "1":
        name = input("Habit name: ")
        habits.append([name, False])   
        print("Added!")

    elif choice == "2":
        if len(habits) == 0:
            print("No habits yet.")
        else:
            for i in range(len(habits)):
                print(i + 1, habits[i][0], "-", "Done" if habits[i][1] else "Not done")

    elif choice == "3":
        for i in range(len(habits)):
            print(i + 1, habits[i][0])
        num = int(input("Which one? "))
        habits[num - 1][1] = True
        print("Marked done!")

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Wrong choice, try again.")