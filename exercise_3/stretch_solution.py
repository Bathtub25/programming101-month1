list_of_numbers = [6, 4, 3, 5, 6, 5, 7, 8, 5, 8, 6]
greater = "greaterthanzero"
less = "lessthanzero"
def findcondition(numbers, condition):

    num=0
    if condition == "greaterthanzero":
        for x in numbers:
            if x >= 0:
                num=num+1
            
    elif condition == "lessthanzero":
        for x in numbers:
            if x <= 0:
                num=num+1
    else:
        print("Invalid Condition")
    print(num)
findcondition(list_of_numbers, greater)
findcondition(list_of_numbers, less)