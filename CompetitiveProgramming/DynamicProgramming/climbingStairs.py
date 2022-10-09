# https://leetcode.com/problems/climbing-stairs/

class Solution:


    def climbStairs(self, n: int) -> int:

        stepCount = {}

        def recurseTopDown(steps):

            if(steps in stepCount):
                return stepCount[steps]

            if(steps < 0):
                return 0

            if(steps == 0):
                return 1

            r1 = recurse(steps - 1)

            r2 = recurse(steps - 2)

            stepCount[steps] = r1+r2

            return r1+r2
        
        #recurseTopDown(n)

        #return stepCount[n]

        if(n==1):
            return 1

        # 1 way for 1 step
        # 2 ways for 2 steps 
        distantWays = [1,2]

        # the no of distant ways for n steps would be = (no of ways for n-1 steps + no of ways for n-2 steps)
        for i in range(2,n):
            distantWays = [distantWays[1], distantWays[0]+distantWays[1]]

        return distantWays[1]

