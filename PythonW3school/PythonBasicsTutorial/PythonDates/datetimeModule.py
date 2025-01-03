import datetime
x = datetime.datetime.now()

print(x)
print(x.year)
# here %A is the directive itself and strftime("%A") formats the date into a string representing the day of week
print(x.strftime("%A"))
