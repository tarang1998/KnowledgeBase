class Solution:

    record = {}

    #Top Down approach  
    def climbStairs(self,n : int ) -> int:

        if(n == 1):
            return 1

        if(n == 2):
            return 2

        if(n in self.record):
            return self.record[n]

        self.record[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return self.record[n]



    #Bottom Up Approcach
    def climbStairsBottomUp(self, n: int) -> int:

        if(n==1):
            return 1

        # 1 way for 1 step
        # 2 ways for 2 steps 
        distantWays = [1,2]

        # the no of distant ways for n steps would be = (no of ways for n-1 steps + no of ways for n-2 steps)
        for i in range(2,n):
            distantWays = [distantWays[1], distantWays[0]+distantWays[1]]

        return distantWays[1]

