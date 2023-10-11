class Solution:

    # Time Complexity : O(len(s)*len(t))
    def numDistinct(self,s: str, t : str) -> int:

        # Not possible to create string t if length of s 
        # is lessaer than t 
        if(len(s)<len(t)):
            return 0
        
        # Key = (i,j)
        # Value = in how many ways we can create t given the combination
        # of indexes (i,j)
        mem = {}


        def dfs(i,j):

            # Base case : The whole string t is formed
            if(j == len(t)):
                return 1

            # Base case : All letters of string s is utilized
            if(i == len(s)):
                return 0

            # Checking if result is already computed
            if((i,j) in mem):
                return mem[(i,j)]

            # If the characters at position i and j match
            # 1. Consider both of them and increment each pointer i and j 
            # 2. Dont consider the character of string s and increment the pointer i
            if(s[i] == t[j]):
                mem[(i,j)] = def(i+1,j+1) + def(i+1,j)
            
            # If characters do not match
            # Increment the pointer to the string s : i
            else:
                mem(i,j) = def(i+1,j)

            return mem[(i,j)]


        return dfs(0,0)




