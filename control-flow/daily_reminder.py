# daily_reminder.py

# Step 1: Prompt for a single task
task = input("Enter your task: ")

# Step 2: Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Step 3: Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 4: Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level"

# Step 5: Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Step 6: Print the customized reminder with explicit f-string format
print(f"Reminder: {reminder}")
