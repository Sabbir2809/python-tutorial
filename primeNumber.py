import math
user_number = int(input("Upper limit for prime: "))

def is_prime(number):
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True

for i in range(2, user_number+1):
    if is_prime(i):
        print(i)





