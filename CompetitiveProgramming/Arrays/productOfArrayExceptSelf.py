class Solution:
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        prefix = 1

        # Looping from the beginning of the array to the end
        # computing the product of all the integers before a certain position  

        for num in nums:
            output.append(prefix)
            prefix *= num 

        suffix = 1

        # Looping from the end of the array to the beginning 
        # computing the product of all the integers after a certain position
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            output[i] *= suffix
            suffix *= num

        return output
class Solution:
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        prefix = 1

        # Looping from the beginning of the array to the end
        # computing the product of all the integers before a certain position  

        for num in nums:
            output.append(prefix)
            prefix *= num 

        suffix = 1

        # Looping from the end of the array to the beginning 
        # computing the product of all the integers after a certain position
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            output[i] *= suffix
            suffix *= num

        return output
