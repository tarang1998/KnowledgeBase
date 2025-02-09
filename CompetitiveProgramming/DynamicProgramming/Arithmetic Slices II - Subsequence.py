from collections import defaultdict

class Solution:

    # Time Complexity : O(n^2)
    # Space Complexity : O(n^2)
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)

        # Initialize a 2D DP array 
        # dp[i][j] denotes the no of arithematic subsequences possible till the index j
        # with the common difference between the elements equal to nums[i] - nums[j]
        dp = [[0]*n for i in range(n)]

        # Initialize a dictionary which will store the indices of the elements in the list
        index = defaultdict(list)
        for i in range(n):
            index[nums[i]].append(i)

        totalSequences = 0 

        # Calculate all the possible sequences 
        # Starting from 1 as the subsequence should have a length of atleast 3 
        for i in range(1,n):
            for j in range(i+1,n):

                # Consider a 3 element sequence 
                # Here i is considered as the mid element, say x 
                # j is considered as the right element, say x+m
                # To find the left element: 2(mid ele) - right_ele
                # 2x - (x+m) = x-m
                leftEle = 2*nums[i] -nums[j]

                # Check for the occurences of the left ele in the map
                for k in index[leftEle]:

                    # Check if the element is in the left hand side of i 
                    if(k<i):
                        # no of possible combinations ending at j with diff : (nums[i]- nums[j])
                        # would be 1 + (no of combinations ending at i with diff : (nums[k] - nums[i]))
                        dp[i][j] += dp[k][i] + 1 

                    # No need to continue if the elements are on the right hand side of i
                    else:
                        break

                totalSequences += dp[i][j]

        return totalSequences 
        