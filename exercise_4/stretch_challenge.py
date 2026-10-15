list_of_numbers = [1, 5, 5, 6, 7, 4]
def reverselist(numbers):
    length=len(numbers)-1
    for i in range(length, -1, -1):
        print(numbers[i])


def find_conditionedreverse(numbers, startindex, endindex ):
    length = len(numbers)-1
    inrange = False
    rangelist = []
    reverselist(numbers[startindex-1:endindex])


 #   for x in numbers:
        #if# x == startindex:
         #   inrange = True
        #    rangelist.append(x)
       # elif x == endindex:
      #      inrange = False
     #       rangelist.append(x)
    #    else: 
   #          if inrange == True:
  #              rangelist.append(x)

   

find_conditionedreverse(list_of_numbers,2, 4)