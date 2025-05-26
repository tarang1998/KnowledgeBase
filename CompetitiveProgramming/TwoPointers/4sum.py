
from collections import defaultdict

class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)

        results = []

        for i in range(len(nums)-3):

            if i>0 and nums[i]==nums[i-1]:
                continue

            nums1 = nums[i]

            for j in range(i+1,len(nums)-2):

                if j-1 != i and nums[j] == nums[j-1]:
                    continue

                nums2 = nums[j]

                left = j+1
                right = len(nums)-1

                while left<right:

                    val = nums1 + nums2 + nums[left] + nums[right]

                    if val > target:
                        right-=1

                    if val < target :
                        left += 1

                    if val == target:
                        results.append([nums1,nums2,nums[left],nums[right]])

                        left += 1
                        right -= 1

                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right] == nums[right+1]:
                            right-=1 

        return results
            



       