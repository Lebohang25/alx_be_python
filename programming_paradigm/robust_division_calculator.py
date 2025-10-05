def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Both arguments must be valid numbers."
    
    try:
        result = num / den
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
