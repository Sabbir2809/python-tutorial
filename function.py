# Return Type Function
def addTwoValue(first, second):
    return first + second

numberOne = 10
numberTwo = 20
# print(f"{numberOne} + {numberTwo} = {numberOne+numberTwo}")
sum = addTwoValue(numberOne, numberTwo)
print(f"{numberOne} + {numberTwo} = {sum}")
print("")

# Void Type Function
print("Start")
def complicatedLogic(num1, num2):
    print(f"You Passed: {num1}, {num2}")

number_1 = 2
number_2 = 3
print("Middle")

complicatedLogic(number_1, number_2)
complicatedLogic(8, 9)
print("End")

