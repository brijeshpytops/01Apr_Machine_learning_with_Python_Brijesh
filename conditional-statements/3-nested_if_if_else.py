age = input("Enter age: ")
age = int(age)

if age >= 18:
    weight = input("Enter weight: ")
    weight = int(weight)
    if  weight>= 50:
        print("You can donate")
    else:
        print("You can not donate")
else:
    print("You can not donate")