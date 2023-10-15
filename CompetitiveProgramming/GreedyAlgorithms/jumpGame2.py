class Solution:

    # Greedy Approach
    def jump(self,nums : List[int]) -> int:

        # Maintain two pointers that indicate the
        # left and the right boundary of the indexes that could be reached 
        # after every iteration
        l = r = 0 

        # Create a farthest pointer to indicate the fathest index that could be 
        # reached from a given set of indices
        farthest = 0

        steps = 0 

        while(r < len(nums)-1):

            # Loop through the given set borderedby l and r 
            # to find farthest index that could be reached
            for i in range(l,r+1):

                farthest = max(farthest, i + nums[i])

            l = r + 1

            r = farthest

            steps += 1

        return steps

                





    # Dynamic Programming Recursive Solution
    def jump1(self, nums: List[int]) -> int:

        # Storing the no of steps required to reach the destination from the index
        # If dest cant be reaced a value of infinity is assigned 
        mem = {}

        def dfs(index):

            # If index has reached the final destination
            if(index == len(nums)-1):
                return 0

            # If index goes beyond the final destination
            if(index >= len(nums)):
                return float('inf')

            # If the value for this index is already computed 
            if(index in mem):
                return mem[index]

            ele = nums[index]

            minSteps = float('inf')

            for i in range( 1 , ele + 1):

                minSteps = min(minSteps,1 + dfs(index + i))

            mem[index] = minSteps

            return mem[index]


        return dfs(0)
        