

def partition(arr, low, high):
    
    #considering the value at the higher end as pivot
    #Could also consider using the middle element or the leftmost element as the pivot
    pivot  = arr[high]
    index = low-1
    
    for i in range(low,high):
        if(arr[i] <= pivot):
            index +=1
            arr[i],arr[index] = arr[index], arr[i]
            
    arr[high], arr[index+1] = arr[index+1], arr[high]
    return index+1;
        
    

def quickSort(arr, low , high):
    
    if(low <high):

        p = partition(arr,low,high)
    
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)
    

def maximumToys(prices, k):
    # Write your code here
    
    quickSort(prices,0,len(prices)-1)
    
    price = 0
    toyCount = 0 
    
    for i in range(0,len(prices)):
        price += prices[i]
        
        if(price>k):
            break
        else:
           toyCount+=1
    
    return toyCount
        

if __name__ == '__main__':

    array = list(map(int, input().rstrip().split()))

    quickSort(array)

    print(array)