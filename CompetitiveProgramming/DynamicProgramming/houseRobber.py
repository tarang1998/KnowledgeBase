#https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:

        dp0 = 0
        dp1 = nums[0]

        #(dp0,dp1)
        # dp0 : If current house isnt selected
        # dp1 : If current house is selected


        for i in range(1,len(nums)):

            t = max(dp0,dp1)
            dp1 = dp0 + nums[i]
            dp0 = t


        return max(dp0,dp1)
