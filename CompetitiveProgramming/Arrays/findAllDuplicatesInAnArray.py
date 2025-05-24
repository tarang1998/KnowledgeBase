class Solution:

    # Time Complexity : O(n)
    # Space Compelxity : O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:

        result = []

        # Use the provided list to mark if a number has already occured 
        # if n has occured assign the element at position n-1 a negative value
        for i in range(len(nums)):

            num = abs(nums[i])

            position = num - 1

            numAtPosition = nums[position]

            if numAtPosition < 0 :
                result.append(num)
            else:
                nums[position] = - nums[position]

        return result

        