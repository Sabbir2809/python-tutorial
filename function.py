# Return Function
def addTwoValue(first, second):
    return first + second

numberOne = 10
numberTwo = 20
# print(f"{numberOne} + {numberTwo} = {numberOne+numberTwo}")
sum = addTwoValue(numberOne, numberTwo)
print(f"{numberOne} + {numberTwo} = {sum}")


# Void Function
print("Start")
def complicatedLogic(first, second):
    print(f"You Passed: {first}, {second}")
    # return first + second * 12 - 4 * 12

number_1 = 2
number_2 = 3
print("Middle")
complicatedLogic(number_1, number_2)
complicatedLogic(8, 9)
print("End")

