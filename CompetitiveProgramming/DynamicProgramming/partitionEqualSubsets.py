class Solution:


    # Using a recursive approach 
    # Time Complexity : O(2^n)
    def canPartitionRecursion(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total/2


        def dfs(i,target):

            if target == 0:
                return True 

            if i == len(nums) or target < 0:
                return False

            return dfs(i+1, target) or dfs(i+1, target - nums[i])


        return dfs(0,target)


    # Using Dynamic Programming (Top - Down )
    # Time Complexity : O(n * target)
    # Space Complexity : O(n * target)
    def canPartitionDP(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total//2

        n = len(nums)

        mem = [[-1] * (target+1) for _ in range(n+1)]

        def dfs(i,target):

            if target == 0:
                return True 

            if i == len(nums) or target < 0:
                return False
            
            if mem[i][target] != -1 :
                return mem[i][target]
            
            mem[i][target] =  dfs(i+1, target) or dfs(i+1, target - nums[i])

            return mem[i][target]

        return dfs(0,target)




    # Using Space Optimized Dynamic Programming
    # Time Complexity : O(n * target)
    # Space Complexity : O(target )
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total/2

        dp = set()
        dp.add(0)

        # dp would hold all the possible sum combinations as we loop through the array backwards
        # Intially, dp = (0)
        # After the first iteration, dp = (0, nums[-1])
        # In the second iteration, dp = (0, nums[-2], nums[-1], nums[-1] + nums[-2])
        # If the target is found during the iterations, return True
        for i in range(len(nums)-1,-1,-1):

            num = nums[i]

            temp = set()

            for j in dp:

                temp.add(j)

                x = j + num

                if x == target:
                    return True

                temp.add(x)

            dp = temp

        return False



                