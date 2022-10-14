class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        arrayCal = [nums[0]]

        result = nums[0]

        for i in range(1,len(nums)):

            ele = nums[i]

            if(arrayCal[i-1]+ nums[i] > nums[i]):
                if(arrayCal[i-1]+ nums[i] > result):
                    result = arrayCal[i-1]+ nums[i]
                arrayCal.append(arrayCal[i-1]+ nums[i])
            else:
                if(nums[i] > result):
                    result = nums[i]
                arrayCal.append(nums[i])

        return result

        










