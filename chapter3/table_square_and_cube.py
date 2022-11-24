nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)

number = int(input("Enter a number that is not less than 5?  "))
if number < 5:
    print("number shuold not be less than five(5)")
elif number >= 5:
    print(f"{'number':<10} {'square':<10} {'cube':<10} ")
    for i in range(number+1):
        print(f"{i:<10} {i**2:<10} {i**3:<10} ")

