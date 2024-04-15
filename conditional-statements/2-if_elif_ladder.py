score = int(input("Enter score: "))

if score >= 0 and score <= 100:
    if score >= 80:
        print("first class")
    elif score >= 60:
        print("Second class")
    elif score >= 40:
        print("Third class")
    else:
        print("Sorr you are failed")
else:
    print("Invalid score.Please enter score between 0 to 100.")


