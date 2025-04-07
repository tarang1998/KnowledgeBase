class Solution:
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mem = {}

        for index,num in enumerate(nums):

            leftOver = target - num 

            if(leftOver in mem):
                return [index,mem[leftOver]]

            mem[num] = index
        