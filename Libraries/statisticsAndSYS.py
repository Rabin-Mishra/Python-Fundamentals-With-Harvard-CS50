# use of statistics and sys libraries in python
import statistics
import sys

print(statistics.mean([22, 33, 44, 55, 66]))

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("My name is ", sys.argv[1])
