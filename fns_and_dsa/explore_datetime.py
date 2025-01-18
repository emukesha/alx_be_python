from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    days = input("Enter the number of days to add to the current date: ")
    days = int(days)
    d = date.today()
    future_date = timedelta(days=days)
    future_date = future_date.strftime("%Y-%m-%d")
    return f"Future date: {future_date}"