class Solution:

    # Dynamic Programming Problem :
    
    # Iterating through all the element in the array 
    # Considering the case where the ith element is the last one to be removed 
    # Thus its contribution would be equal to 1*nums[i]*1

    # This helps to divide the problem into subproblems
    # The left array from index L:i-1 
    # The right array from index i+1:R
    # Follow the same approach for both sub arrays
    # In this case the right subarray is gauranted to have boundary values as 3 and 1
    # And left subarray has boundaries 1 and 3

    # Time Complexity : O(n^3)
    # n^2 combinations are possible with (l,r)
    # And we are iterating 
    def maxCoins(self, nums: List[int]) -> int:

        # Adding the left and the right boundaries
        nums = [1] + nums + [1]


        mem = {}

        def dfs(l,r):

            # Base case if the left and right pointer have crossed each other
            # No elements left
            if l>r:
                return 0 

            # If value already computed 
            if (l,r) in mem:
                return mem[(l,r)]

            maxValue = 0

            # Iterating through each element assuming the 
            # one to be picked is going to removed last in the array
            for i in range(l,r+1):

                # Computing the values based on the fixed boundaries
                coins = nums[l-1] * nums[i] * nums[r+1]

                result = coins + dfs(l,i-1) + dfs(i+1,r)

                if(result > maxValue):
                    maxValue = result 

            mem[(l,r)] = maxValue
            return maxValue

        return dfs(1,len(nums)-2)



       