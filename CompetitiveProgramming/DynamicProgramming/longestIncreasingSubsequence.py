class Solution:

    maxValue = None

    mem = None 

    # Time Complexity : O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:

        self.maxValue = 1 
 
        self.mem = {}
        self.mem[len(nums)-1] = 1

        for i in range(len(nums)-2 , -1, -1):

            self.mem[i] = 1

            for j in range(i+1,len(nums)):

                if(nums[i] < nums[j]):

                    if(1 + self.mem[j] > self.mem[i]):
                        self.mem[i] = 1 + self.mem[j]

                        if(self.mem[i] > self.maxValue):
                            self.maxValue = self.mem[i]

        return self.maxValue



        