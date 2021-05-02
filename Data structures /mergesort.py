arr = [3, 12, 31, 5, 18, 17, 16]
def mergesort(data):
  if len(data) > 1:
    mid = len(data) // 2
    leftarr = data[:mid]
    rightarr = data[mid:]

    mergesort(leftarr)
    mergesort(rightarr)

    i = 0
    j = 0
    k = 0

    while i < len(leftarr) and j < len(rightarr):
      if leftarr[i] < rightarr[j]:
        data[k]= leftarr[i]
        i += 1
      else:
        data[k] = rightarr[j]
        j += 1
      k += 1
    
    while i < len(leftarr):
      data[k]= leftarr[i]
      i += 1
      k += 1
    
    while j < len(rightarr):
      data[k] = rightarr[j]
      j += 1
      k += 1
  
print(arr)
mergesort(arr)
print(arr)
