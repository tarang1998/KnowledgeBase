



def binarySearch(arr,low,high,ele):


    while(low<=high):

        mid = (low+high) // 2

        if(ele > arr[mid]):
            low = mid+1

        elif(ele < arr[mid]):
            high = mid-1

        else:
            return mid
            
    return -1






#Array should be sorted
arr = [2, 3, 4, 10, 40]
x = 10
  
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

print(result)
