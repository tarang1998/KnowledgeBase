
class Solution:

    def canPartition(self, nums: List[int]) -> bool:

        if(sum(nums)%2 != 0 ):
            return False

        target = sum(nums)//2

        dp = set()
        dp.add(0)

        for i in range(len(nums)-1 , -1, -1):

            temp = set()

            for j in dp:

                x = j + nums[i]

                if(x == target):
                    return True 

                temp.add(j)

                if(x < target):
                    temp.add(x)

                dp = temp

        return False




        
        