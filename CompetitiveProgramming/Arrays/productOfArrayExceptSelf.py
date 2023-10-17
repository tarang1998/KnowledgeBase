class Solution:

    # Time Complexity : O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        suffix = [1]

        prefix = [1]

        for i in range(len(nums)):
            prefix.append(nums[i] * prefix[-1])
            suffix.append(nums[~i] * suffix[-1])

        result = []

        for i in range(len(nums)):

            result.append(prefix[i]*suffix[len(nums)-i-1])

        return result


        