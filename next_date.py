
def validate_date(day, month, year):
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}. It must be between 1 and 12.")
    days_in_current_month = days_in_month(month, year)
    if not (1 <= day <= days_in_current_month):
        raise ValueError(f"Invalid day: {day}. {month:02d}-{year} has only {days_in_current_month} days.")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28

def next_date(date_str):
    day, month, year = map(int, date_str.split('-'))
    validate_date(day, month, year)
    days_in_current_month = days_in_month(month, year)
    if day < days_in_current_month:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1  # Move to the next year
        else:
            month += 1  # Move to the next month
    # Format the next date as dd-mm-yyyy
    return f'{day:02d}-{month:02d}-{year}'
