# Prompt for the task description
task = input("Enter your task: ")

# Initialize variables for priority and time-bound with empty strings
priority = ''
time_bound = ''

# Loop until a valid priority is entered
while priority not in ['high', 'medium', 'low']:
    priority = input("Priority (high/medium/low): ").lower()

# Loop until a valid time-bound response is entered
while time_bound not in ['yes', 'no']:
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate the reminder message using match case for priority and if for time-bound
match priority:
    case 'high':
        if time_bound == 'yes':
            message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            message = f"Note: '{task}' is a high priority task. Please ensure to address it promptly."
    case 'medium':
        if time_bound == 'yes':
            message = f"Reminder: '{task}' is a medium priority task that needs to be completed today."
        else:
            message = f"Note: '{task}' is a medium priority task. Consider completing it soon."
    case 'low':
        if time_bound == 'yes':

            #Checks for Provide a Customized Reminder
            message = f"Reminder: '{task}' is a low priority task with a deadline today. Address if possible."
        else:
            message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

# Print the generated message


print("\n" + message)
