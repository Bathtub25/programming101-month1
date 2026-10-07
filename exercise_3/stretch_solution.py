list_of_numbers = [6, 4, 3, 5, 6, 5, 7, 8, 5, 8, 6]
wantednum=8
def find_max_from_list_of(numbers, targetnum):
    # function definition
    instances = 0
    if targetnum == None or numbers == None:

        print("Invalid Input")
        return
    for x in numbers:
        if (x == targetnum):
            instances = instances + 1


    if instances == 1:
        print("Number occurs", instances, "time")
    else:
        print("Number occurs", instances, "times")

find_max_from_list_of(list_of_numbers, wantednum)
