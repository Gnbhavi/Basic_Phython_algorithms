#Insert_Sort_Algorithm
list_to_sort = [10,7,5,3,77,42,21]
#Input list to be sorted
n = len(list_to_sort)
# n to find number of elements in list
for i in range(1,n):
    #i is intialized to 0.
    #for loop is run for n times(i.e 0 to n-1).
    #Finding the minimum strating from ith position in list to last position
    for j  in range(i,0,-1):
        if list_to_sort[j] < list_to_sort[j-1]:
            list_to_sort[j] , list_to_sort[j-1] = list_to_sort[j-1] , list_to_sort[j]
    #Comparing the jth positon with the neighbour and interchanging if its bigger
 #Repeating the procedure for every i
print(list_to_sort)
