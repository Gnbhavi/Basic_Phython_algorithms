#Selection_Sort_Algorithm
list_to_sort = [10,7,5,3,77,42,21]
#Input list to be sorted
n = len(list_to_sort)
# n to find number of elements in list
for i in range(n):
    #i is intialized to 0.
    #for loop is run for n times(i.e 0 to n-1).
    mini = list_to_sort[i]
    pos  = i
    #Finding the minimum strating from ith position in list to last position
    for j in range(i,n):
        if list_to_sort[j] < mini:
            mini = list_to_sort[j]
            pos  = j
    #Interchanging the ith positon with the minimum value position
    list_to_sort[i] , list_to_sort[pos] = list_to_sort[pos] , list_to_sort[i]
    #Repeating the procedure for every i
print(list_to_sort)

