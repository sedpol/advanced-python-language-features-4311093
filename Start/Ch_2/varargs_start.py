# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions


# TODO: define a function that takes variable arguments
def addition(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


# TODO: pass different arguments
print(addition(6 + 9 + 10))

# TODO: pass an existing list
numsToSum = [12, 14, 434, 22]
print(addition(*numsToSum))