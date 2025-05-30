import bisect

class Solution:

    # Using the bisect library 
    # Time Complexity : O(nlogn)
    def lengthOfLIS(self, nums: List[int]) -> int:

        tails = [nums[0]]

        for i in range(1, len(nums)):

            num = nums[i]

            # Find the leftmost position in the tails array where the current number : num can be placed.
            pos = bisect.bisect_left(tails, num)

            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)


    # Time Complexity : O(nlogn)
    # Using binary search
    def lengthOfLIS2(self, nums: List[int]) -> int:

        tails = [nums[0]]

        for i in range(1,len(nums)):

            num = nums[i]

            left = 0  
            right = len(tails) 

            while left<right:
                
                mid = (left + right)//2 

                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid  

            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num  

        return len(tails)
                

    # Time Complexity : O(n^2)
    def lengthOfLIS1(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        lis = 1 

        for i in range(len(nums)-1,-1,-1):
            temp = [dp[i]]
            for j in range(i+1,len(nums)):

                if nums[i] < nums[j]:
                    temp.append(dp[i]+dp[j])

            dp[i] = max(temp)

            lis = max(lis,dp[i])

        return lis

        