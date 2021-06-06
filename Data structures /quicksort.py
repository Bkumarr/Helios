#Implement quicksort

# dlist = [60, 93, 28, 50, 21, 39, 56]
dlist = [91, 45, 23, 67, 12, 21, 60, 90, 24, 43, 22]


def partition(datavalue, first, last):

  pivot_index = first
  pivotpos = datavalue[pivot_index]
  upper = last
  lower = pivot_index + 1

  while lower <= upper:

    
          #Advance the lower 
    while lower < len(datavalue) and datavalue[lower] < pivotpos:


      lower +=1
            #Advance the upper
    while datavalue[upper] > pivotpos:
      upper -=1

            #find for crossing point
    if (lower <= upper):

      datavalue[lower], datavalue[upper] = datavalue[upper], datavalue[lower]

      #when the split point is found
  datavalue[upper], datavalue[pivot_index] = datavalue[pivot_index], datavalue[upper]

    
  return upper


def quick_sort(dset, first, last):
    
  if (first < last):
      
    pivotIdx = partition(dset, first, last)
  
    quick_sort(dset, first, pivotIdx-1)
    quick_sort(dset, pivotIdx+1, last)


quick_sort(dlist, 0, len(dlist)-1)
print(f'Sorted array: {dlist}')


#Method 2
# dlist = [60, 93, 28, 50, 21, 39, 56]


        
# def partition(datavalue, first, last):
#     pivot_index = first
#     pivotpos = datavalue[pivot_index]
#     upper = last
#     lower = pivot_index + 1
    
#     done = False
#     while not done:
#         while (datavalue[upper] > pivotpos and upper >= lower):
#             upper -=1
        
#         while (datavalue[lower] < pivotpos and upper >= lower):
#             lower +=1
            
#         if (upper <= lower):
#             done = True
#         else:
#             datavalue[lower], datavalue[upper] = datavalue[upper], datavalue[lower]
            
#     datavalue[pivot_index], datavalue[upper] = datavalue[upper], datavalue[pivot_index]
    
#     return upper

# def quick_sort(dset, first, last):
    
#     if (first < last):
#         pivot = partition(dset, first, last)
    
#         quick_sort(dset, first, pivot-1)
#         quick_sort(dset, pivot+1, last)
        
        
# quick_sort(dlist, 0, len(dlist)-1)
# print(f'Sorted array: {dlist}')