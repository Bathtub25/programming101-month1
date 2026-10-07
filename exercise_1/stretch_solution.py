list_of_numbers = [7,9,11,14,20,44]

def find_max_from_list_of(numbers):
    # function definition
    maxNum = numbers[0]
    for x in numbers:
        maxNum = betterOf(maxNum, x)

    print("Largest number is ", maxNum)

def betterOf(a,b):
    if b > a:
        return b
    else:
        return a
   
find_max_from_list_of(list_of_numbers)