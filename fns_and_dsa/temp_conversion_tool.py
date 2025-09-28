# temp_conversion_tool.py

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature converted to Celsius
    """
    # Accessing global variable (read-only, no need for global keyword)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature converted to Fahrenheit
    """
    # Accessing global variable (read-only, no need for global keyword)
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    print("Temperature Conversion Tool")
    print("=" * 30)
    
    try:
        # Get temperature input from user
        temp_input = input("Enter temperature value: ")
        
        # Validate if input is numeric
        try:
            temperature = float(temp_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        # Get temperature unit from user
        unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").strip().upper()
        
        # Perform conversion based on unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"\n{temperature}°F = {converted_temp:.2f}°C")
            print(f"Conversion used: ({temperature} - 32) × {FAHRENHEIT_TO_CELSIUS_FACTOR:.4f}")
            
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"\n{temperature}°C = {converted_temp:.2f}°F")
            print(f"Conversion used: ({temperature} × {CELSIUS_TO_FAHRENHEIT_FACTOR:.1f}) + 32")
            
        else:
            print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Additional function to demonstrate variable scope
def demonstrate_scope():
    """
    Demonstrate variable scope by showing global vs local variables.
    """
    print("\n" + "=" * 40)
    print("Variable Scope Demonstration")
    print("=" * 40)
    
    # Show global variables are accessible
    print(f"Global FAHRENHEIT_TO_CELSIUS_FACTOR: {FAHRENHEIT_TO_CELSIUS_FACTOR}")
    print(f"Global CELSIUS_TO_FAHRENHEIT_FACTOR: {CELSIUS_TO_FAHRENHEIT_FACTOR}")
    
    # Demonstrate that we can't modify globals without global keyword
    def try_modify_global():
        # This would create a local variable, not modify the global
        FAHRENHEIT_TO_CELSIUS_FACTOR = "local value"
        print(f"Inside function (local): FAHRENHEIT_TO_CELSIUS_FACTOR = {FAHRENHEIT_TO_CELSIUS_FACTOR}")
    
    try_modify_global()
    print(f"Outside function (global unchanged): FAHRENHEIT_TO_CELSIUS_FACTOR = {FAHRENHEIT_TO_CELSIUS_FACTOR}")

if __name__ == "__main__":
    main()
    demonstrate_scope()
