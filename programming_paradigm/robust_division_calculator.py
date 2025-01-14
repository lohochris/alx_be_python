def safe_divide(numerator, denominator):
    """
    Safely performs division, handling errors like division by zero and non-numeric inputs.

    :param numerator: The numerator for the division.
    :param denominator: The denominator for the division.
    :return: Result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Attempt division
        result = num / den
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Both inputs must be numeric."

