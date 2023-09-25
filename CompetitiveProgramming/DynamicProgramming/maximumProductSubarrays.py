class Solution:
        

    # Time Complexity : O(n), Space Complexity : O(1)
    def maxProduct1(self, nums: List[int]) -> int:

        maxValue = float('-inf')

        prod = 1

        # Parsing the array from left to right 
        # The idea is to lookout for odd no of negative numbers
        for num in nums:

            prod *= num

            maxValue = max(prod, maxValue)

            # If a zero is encountered reset the the product to 1
            if(prod == 0 ):
                prod = 1

        prod = 1

        #Parsing the array from right to left
        for i in range(len(nums)-1,-1,-1):

            prod *= nums[i]

            maxValue = max(prod,maxValue)

            if(prod == 0 ):
                prod = 1

        return maxValue



    # Time Complexity : O(n), Space Complexity : O(1)
    def maxProduct(self, nums: List[int]) -> int:

        result = max(nums)

        #Storing currMin and currMax for all the subarrays
        #from left to right
        #and capturing max value after each instance
        currMin = 1
        currMax = 1

        for num in nums:

            temp = currMax

            currMax = max(num * temp, num * currMin, num)
            currMin = min(num * temp, num * currMin, num)
            result = max(result,currMax)

            print(num,currMin,currMax)

        return result




        