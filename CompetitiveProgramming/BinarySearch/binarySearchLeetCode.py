class Solution:

    def recurse(self,nums: List[int], target : int, low : int, high :int):

        left = 0 

        right = len(nums) - 1

        while(left<=right):

            mid = (left+right)//2

            if(target == nums[mid]):
                return mid

            if(target < nums[mid]):
                right -= 1
            else:
                left += 1

        
        return -1



    def recurse1(self,nums: List[int], target : int, low : int, high :int):

        if(low <= high):

            mid = (low + high)//2

            if(target == nums[mid]):
                return mid

            if(target < nums[mid]):
                return self.recurse(nums,target,low,mid-1)
            else:
                return self.recurse(nums,target,mid+1,high)


        else:
            return -1 

    def search(self, nums: List[int], target: int) -> int:

        low = 0 

        high = len(nums) - 1

        return self.recurse(nums, target, low, high)








