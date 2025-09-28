from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("Current date and time: %Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(future_date.strftime("Future date: %Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
