from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")

def future_date():
    nums = input("Enter the number of days to add to the current date: ")
    nums = int(nums)
    d = date.today()
    days = timedelta(days=nums)
    return f"Future date: {d + days}"