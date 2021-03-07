def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

even_numbers = []
user_input = int(input("Limit: "))

for num in range(0, user_input + 1):
    if isEven(num):
        even_numbers.append(num)

print(f"Even number: {even_numbers}")
print("Finished")

firends_list = ["Sabbir", "Komol", "Salkin", "Mizan", "Maruf", "Shafe", "Zafrin", "Sajia"]

# for item in firends_list:
for item in range(0, len(firends_list)):
    if item == "Maruf":
        break
    if item == "Salkin":
        continue
    print(firends_list[item])
print("Finished")

for i in range(0, 10+1, 2):
    print(i)
print("Finished")
