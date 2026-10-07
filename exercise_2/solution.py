list_of_numbers = [7,9,11,14,20,44]

def find_max_from_list_of(numbers):
    # function definition
    maxNum = numbers[0]
    for x in numbers:
        if (x < maxNum):
            maxNum = x

    print("Smallest number is ", maxNum)

def betterOf(a,b):
    if b > a:
        return True
    else:
        return False

find_max_from_list_of(list_of_numbers)