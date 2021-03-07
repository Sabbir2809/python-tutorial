def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

even_numbers = []
odd_numbers = []
starting = 0
user_input = int(input("Limit: "))

while starting <= user_input:

    if isEven(starting):
        # print(f"{starting} is Even")
        even_numbers.append(starting)
    # else:
    #     print(f"{starting} is Odd")
    else:
        odd_numbers.append(starting)
    starting = starting + 1

print(f"Even number: {even_numbers}")
print(f"Odd number: {odd_numbers}")


