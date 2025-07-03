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

    # Final customized reminder using f-string directly in print
    if time_bound == 'yes':
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()
