num = (input("Enter numbers: "))
num_revasser = num[::-1]

if num == num_revasser:
    print(f'Number {num} is a palindrom')
else:
    var = num != num_revasser
    print(f'Number {num} is not a palindrom')