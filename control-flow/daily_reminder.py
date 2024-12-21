task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    
    case "high":
        reminder = f"{task} is a {priority} priority task that requires immediate attention today!"
        if time_bound == "yes":
            print(reminder)
        print(reminder)
    case "medium":
        reminder = f"{task} is a {priority} priority task that requires immediate attention today!"
        if time_bound == "yes":
            print(reminder)
        print(reminder)
    case "low":
        reminder = f"{task} is a {priority} priority task that requires immediate attention today!"
        if time_bound == "yes":
            print(reminder)
        print(reminder)