from math import factorial

number = int(input("Enter a number "))
total = 1
if number < 0:
    print("those not have a factorial")

elif number == 0:
    print("factorail is 1")
else:
    for count in range(number, 0, -1):
        total *= count
    print(total)