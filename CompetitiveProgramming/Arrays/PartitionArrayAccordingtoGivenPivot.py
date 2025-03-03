class Solution:
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:


        left, right = [],[]

        for num in nums:
            if(num < pivot):
                left.append(num)
            elif(num > pivot):
                right.append(num)
        

        return left + [pivot]*(len(nums)-len(left)-len(right)) + right
        