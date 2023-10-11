class Solution:


    # Time Complexity : O(len(word1) * len(word2))
    # Space Complexity : O(len(word1) * len(word2)). Can be improved to O(len(word2))
    def minDistance(self, word1: str, word2: str) -> int:


        # Creating a 2-D array where the cell i,j indicates
        # The no of operations needed to match the strings
        # word1[i:] and word2[j:]
        cache = [[float('inf')] * (len(word2)+1) for i in range(len(word1) + 1)]

        # The last column and the last row specify empty string

        # Filling the last column of the mem 2-D array
        # Eg j=len(word2) i = 0
        # No of operations required to convert word[i:] to empty string
        for i in range(0,len(word1)+1):
            cache[i][len(word2)] = len(word1) - i

        # Filling the last row of the mem 2-D array
        for j in range(0,len(word2)+1):
            cache[len(word1)][j] = len(word2) - j 

        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):

                if(word1[i] == word2[j]):
                    # In this case no operations need to be performed
                    # Proceed to the next sub operation
                    cache[i][j] = cache[i+1][j+1]

                else:
                    # In this case one of the operation needs to be performed
                    # 1. Insertion : We are going to insert the jth element of
                    # word2 into word1
                    # Pointers shift accordingly : (i,j+1)

                    # 2. Deletion : We are deleting the ith character
                    # Pointer shift : (i+1,j)

                    # 3. Replace : We replace the ith character of word1 with
                    # jth character of word2
                    # Pointer shift : (i+1,j+1)
                    cache[i][j] = 1 + min(cache[i][j+1],cache[i+1][j],cache[i+1][j+1])
        
        return cache[0][0]






                


