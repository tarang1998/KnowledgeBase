class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        result = []

        td = float('inf')
        result = None

        nums = sorted(nums)

        for i,num in enumerate(nums):

            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left<right:

                val = nums[left] + nums[right] + num 

                if target == val:
                    return target


                if val < target:
                    d = target - val
                    if d < td:
                        td = d
                        result = val 
                    left += 1
            

                if val > target:
                    d = val - target
                    if d < td:
                        td = d
                        result = val 
                    right -=1


        return result

                    

                

                



        