# Exercise 1 - Find max
list_of_numbers = [7,9,11,14,20,44]

def find_max_from_list_of(numbers):
    # function definition
    maxNum = 0
    for x in numbers:
        if (x < maxNum):
            maxNum = x

    print("Largest number is ", maxNum)

find_max_from_list_of(list_of_numbers)
