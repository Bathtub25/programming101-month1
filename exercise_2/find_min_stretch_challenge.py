list_of_numbers = [7,9,11,14,20,44]
def find_min_from_list_of(numbers):
    # function definition
    minNum = numbers[0]
    for x in numbers:
        minNum = betterOf(minNum, x)

    print("Smallest number is ", minNum)

def betterOf(a,b):
    if b < a:
        return b
    else:
        return a
   
find_min_from_list_of(list_of_numbers)