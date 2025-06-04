class Solution:
    
    # Time Complexity : O(n)
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        destination = n-1

        for i in range(n-2,-1,-1):
            if i + nums[i] >= destination:
                destination = i
        
        if destination == 0:
            return True
        else:
            return False

    # Time Complexity : O(n^2)
    def canJump1(self, nums: List[int]) -> bool:

        n = len(nums)
        canJumpFromPosition = [False]*n
        canJumpFromPosition[n-1] = True
        for i in range(n-2,-1,-1):
            steps = nums[i]

            for j in range(1,steps+1):
                if i + j > n-1:
                    break
                if canJumpFromPosition[i+j]:
                    canJumpFromPosition[i] = True
                    break
        return canJumpFromPosition[0]
        