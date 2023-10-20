class Solution:

    # Using the Dutch Flag Algorithm
    # This algorithm sort the array in 1 iteration 
    # and in place
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def sortColors(self, nums: List[int]) -> None:

        # The algorithm will use 3 pointers 
        # low, mid and high
        # All elements from [0,low-1] would be 0
        # All elements from [low,mid-1] would be 1
        # All the elements from [mid,high] would be unsorted 
        # All the elements from [high+1,n) would ne 2

        # Initially the array is unsorted 
        low = 0 
        mid = 0 
        high = len(nums)-1

        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while(mid <= high):
            # If num = 0 we will swap the low and mid elememts 
            # Then increment the mid pointer and the low pointer 
            if nums[mid] == 0:
                swap(low,mid)
                low += 1
                mid += 1

            # If num = 1 
            # Increment the mid pointer 
            elif nums[mid] == 1:
                mid += 1

            # If num = 2 swap the mid pointer anf the high pointer
            # Decrement the high pointer
            else:
                swap(mid,high)
                high -= 1


    # Store the occurrences of 0,1,2 in a dictionary
    # Construct an array from the dictionary
    # Time Complexity : O(2n) -> O(n)
    # Space Complexity : O(1)
    def sortColors1(self, nums: List[int]) -> None:

        # Storing the occurences of 0,1,2
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        # Constructing the array with 0's
        for i in range(count[0]):
            nums[i] = 0 

        # Constructing the array with 1's
        for i in range(count[0],count[0] + count[1]):
            nums[i] = 1

        # Constructing the array with 2's
        for i in range(count[0]+count[1], count[0]+count[1]+count[2]):
            nums[i] = 2


        

    # Brute Force Approach
    # Sort the given array
    # Time Complexity : O(nlogn)
    # Space Complexity : O(n)
    def sortColors2(self, nums: List[int]) -> None:

        nums.sort()


       

        