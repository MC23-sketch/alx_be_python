def main():
    # Prompt for task description
    task = input("Enter your task: ").strip()

    # Loop to ensure valid priority input
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Please enter a valid priority: high, medium, or low.")

    # Loop to ensure valid yes/no input for time sensitivity
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Please answer 'yes' or 'no'.")

    # Match-case for priority handling
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has an undefined priority"

    # Add time sensitivity message
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Print the final customized reminder
    print(f"Reminder: {message}")


if __name__ == "__main__":
    main()
