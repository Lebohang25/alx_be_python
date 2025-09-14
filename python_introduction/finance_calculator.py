# finance_calculator.py

def main():
    # Prompt user for monthly income and expenses
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))
    
    # Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses
    
    # Project annual savings with 5% interest
    annual_savings_without_interest = monthly_savings * 12
    interest_earned = annual_savings_without_interest * 0.05
    projected_annual_savings = annual_savings_without_interest + interest_earned
    
    # Output the results
    print(f"Your monthly savings are: ${monthly_savings:.2f}")
    print(f"Projected annual savings with interest: ${projected_annual_savings:.2f}")

if __name__ == "__main__":
    main()
