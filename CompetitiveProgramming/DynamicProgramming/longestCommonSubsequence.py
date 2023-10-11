class Solution: 

    # Time Complexity : O(m * n)
    # Memory Optimized Solution : O(n)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        prevRow = [0] * (n+1)
        currRow = [0] * (n+1)

        for i in range(1,m+1):
            for j in range(1,n+1):
                if(text1[j-1] == text2[i-1]):
                    currRow[j] = 1+prevRow[j-1]
                else:
                    currRow[j] = max(prevRow[j],currRow[j-1])

            prevRow = currRow.copy()

        return prevRow[-1]

