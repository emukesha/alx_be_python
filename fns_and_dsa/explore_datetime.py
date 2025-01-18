from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    future_date = input("Enter the number of days to add to the current date: ")
    future_date = int(future_date)
    d = date.today()
    d = d.strftime("%Y-%m-%d")
    days = timedelta(days=future_date)
    return f"Future date: {d + days}"