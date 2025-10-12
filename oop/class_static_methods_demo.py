# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not access class or instance attributes/methods.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Can access and modify class attributes using the cls parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
