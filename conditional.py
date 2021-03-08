marks = int(input("What is your marks in programming: "))

def show_grade(grade):
    print(f"You got: {grade}")

if marks >= 80:
    show_grade("A+")
elif marks < 80 and marks >= 70:
    show_grade("A")
elif marks < 70 and marks >= 60:
    show_grade("A-")
elif marks >= 33:
    show_grade("Passed")
else:
    show_grade("F")
print("Finished")


marks = int(input("What is your marks: "))

if marks > 80 or marks < 33:
    print("Your are very good or very bad")
    if marks > 80:
        print("Excellent")
    else:
        print("Not so good!")
else:
    print("You are okay")


number = int(input("Give a number: "))

isGood = number >= 80
message = "The number is grater than or equals 80: "+ str(isGood)
# print(f"the number is grater than or quals 80: {theUser_isGood}")
print(message)