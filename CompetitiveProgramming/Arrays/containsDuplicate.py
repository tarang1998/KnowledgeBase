class Solution:

    # Time Complexity : O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:

        count = {}


        for num in nums:

            if(num in count):
                return True

            count[num] = 1

        return False
