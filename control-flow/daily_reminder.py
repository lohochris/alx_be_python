# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"The task '{task}' is of HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is of MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is of LOW priority."
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
        exit()

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the customized reminder
print(reminder)
