class Solution:

    # Dynamic Programming 
    # Bottom Approach
    # Time Complexity : O(len(s1) * len(s2))
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if(len(s1) + len(s2) != len(s3)):
            return False

        # dp[i][j] indicates if the word s3 can be formed using 
        # i elements of the string s1
        # and j elements of the string s2
        dp = [[False] * (len(s2)+1) for i in range(len(s1) + 1)]

        dp[len(s1)][len(s2)] = True 

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):

                # if ith element of s1 matches i+j th element of s3
                # Check if s3 can be formed by the combination of i+1 elements of s1 and j elements of s2
                if(i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]):
                    dp[i][j] = True
                
                # if jth element of s2 matches i+j th element of s3
                # Check if s3 can be formed by the combination of i elements of s1 and j+1 elements of s2
                if(j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]):
                    dp[i][j] = True

        return dp[0][0]




    # Recursive and Back Tracking Solution
    # Time Complexity : O(len(s1) * len(s2))
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:

        # The sum of letters ins s1 and s2 should be equal to s3
        if(len(s1) + len(s2) != len(s3)):
            return False

        mem = {}

        def parse(i,j):

            # If all the words have been parsed we we able to form s3 
            if(i == len(s1) and j == len(s2)):
                return True

            # If s1 has been parsed
            # Check if the remainder words in s2 make up s3
            if(i == len(s1)):
                return s2[j:] == s3[i+j:]

            # If s2 has been parsed
            # Check if the remainder words in s1 make up s3
            if(j == len(s2)):
                return s1[i:] == s3[i+j:]

            # If path already computed that means formation of s3 is not possible
            # With this specific combination 
            if((i,j) in mem):
                return False
            
            # If letters of s1 and s3 match 
            # increment the pointer of s1
            # If the result is found then return True
            if(s1[i] == s3[i+j]):
                res = parse(i+1,j)
                if(res):
                    return True
                mem[(i,j)] = res

            # If letters of s2 and s3 match 
            # increment the pointer of s2
            # If the result is found then return True
            if(s2[j] == s3[i+j]):
                res = parse(i,j+1)
                if(res):
                    return True
                mem[(i,j)] = False

            # If letters from both words dont match the letter from s3
            # Formation of the string s3 is not possible
            return False

        return parse(0,0)

            

        