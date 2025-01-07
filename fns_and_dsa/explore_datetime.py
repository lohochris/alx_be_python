from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculate the future date by adding a specified number of days to the current date.
    
    Args:
        current_date (datetime): The current date and time.
        days_to_add (int): Number of days to add to the current date.
    
    Returns:
        datetime: The future date.
    """
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    """
    Main function to handle the script's functionality.
    """
    # Part 1: Display the current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

if __name__ == "__main__":
    main()
