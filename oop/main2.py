# main.py

from class_static_methods_demo import Calculator

def main():
    # Using the static method - no access to class state
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    print("-" * 30)  # Separator for clarity

    # Using the class method - has access to class attributes
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

    print("\n" + "="*50)
    print("Additional demonstrations:")

    # Demonstrating that static methods can be called on instances too
    calc_instance = Calculator()
    sum_instance = calc_instance.add(20, 3)
    print(f"Static method called on instance - sum: {sum_instance}")

    # Class method called on instance - still accesses class attribute
    product_instance = calc_instance.multiply(20, 3)
    print(f"Class method called on instance - product: {product_instance}")

if __name__ == "__main__":
    main()
