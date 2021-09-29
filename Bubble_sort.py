#import numpy
#Selection_Sort_Algorithm
list_to_sort = [10,7,5,3,77,42,21]
#Input list to be sorted
n = len(list_to_sort)
# n to find number of elements in list
for i in range(n):
    #i is intialized to 0.
    #for loop is run for n times(i.e 0 to n-1).
    for j in range(n-i-1):
        #Comparing with the neighour and interchanges if its less
        if list_to_sort[j+1] < list_to_sort[j]:
            list_to_sort[j+1] , list_to_sort[j] = list_to_sort[j] , list_to_sort[j+1]
    #Interchanging the ith positon with the minimum value position
    #Repeating the procedure for every i
print(list_to_sort)

