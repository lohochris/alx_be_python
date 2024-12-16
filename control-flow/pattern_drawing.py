# Prompt the user to enter a positive integer
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
    exit()

# Draw the square pattern
row = 0  # Initialize the row counter
while row < size:  # Outer loop for rows
    for _ in range(size):  # Inner loop for columns
        print("*", end="")  # Print asterisks side by side
    print()  # Move to the next line after each row
    row += 1  # Increment the row counter
