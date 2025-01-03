'''
The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
'''

import datetime

x = datetime.date(2024, 5, 17)
print(x)

# Create a date object for a specific date
date_object = datetime.date(2024, 5, 14)
print("Date:", date_object)

# Get today's date
today = datetime.date.today()
print("Today's Date:", today)

# Create a date object from a string
date_str = "2024-05-14"
date_from_string = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
print("Date from string:", date_from_string)
