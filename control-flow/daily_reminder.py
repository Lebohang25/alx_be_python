# daily_reminder.py
def main():
    # Prompt user for task details
    task = input("Enter your priority task for today: ")
    priority = input("Enter the task priority (high, medium, low): ").lower()
    time_bound_input = input("Is the task time-bound? (yes or no): ").lower()
    
    # Convert time-bound input to boolean
    time_bound = time_bound_input == 'yes'
    
    # Process based on priority using match case
    match priority:
        case "high":
            if time_bound:
                reminder = f"High priority task: {task} that requires immediate attention today!"
            else:
                reminder = f"High priority task: {task} should be your focus today."
        case "medium":
            if time_bound:
                reminder = f"Medium priority task: {task} is time-bound and needs your attention soon."
            else:
                reminder = f"Medium priority task: {task} is important but not urgent."
        case "low":
            if time_bound:
                reminder = f"Low priority task: {task} is time-sensitive; try to address it if possible."
            else:
                reminder = f"Low priority task: {task} can be done when you have free time."
        case _:
            reminder = "Invalid priority level entered. Please restart with high, medium, or low."
    
    # Print the reminder
    print("\n--- Today's Reminder ---")
    print(reminder)

if __name__ == "__main__":
    main()
