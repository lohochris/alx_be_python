def safe_divide(numerator, denominator):
    """
    Perform division with error handling.
    :param numerator: The numerator as a string.
    :param denominator: The denominator as a string.
    :return: The result of the division or an appropriate error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Perform the division
        return f"The result of the division is {num / denom:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."
