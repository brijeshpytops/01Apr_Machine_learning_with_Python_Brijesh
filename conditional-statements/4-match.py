"""
In Python, match is a feature introduced in version 3.10 as part of the pattern matching syntax. Pattern matching is a way to perform more complex conditional logic based on the structure of data. It's especially useful when dealing with nested structures like lists, dictionaries, and custom data types.

syntax:

match expression:
    case pattern1:
        # code block to execute if expression matches pattern1
    case pattern2:
        # code block to execute if expression matches pattern2
    case _:
        # code block to execute if expression matches none of the above patterns

"""

# day = int(input("Enter day : "))
from datetime import datetime
current_date_time = datetime.now()

# current_day = current_date_time.day # month day

day = current_date_time.weekday()

if day <= 6 and day >= 0:
    match (day+1):
        case 1:
            print("Today is Monday")
        case 2:
            print("Today is Tue")
        case 3:
            print("Today is Wed")
        case 4:
            print("Today is Thu")
        case 5:
            print("Today is Fri")
        case 6:
            print("Today is Sat")
        case 7:
            print("Today is Sun")
        case _:
            print("Invalid day")

else:
    print("Invalid day")