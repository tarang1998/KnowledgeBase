class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        # Dictionary to calculate the frequency of 
        # upper case alphabets in the window substring 
        count = {}

        l = 0 

        result = 0 

        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r],0)

            # If the diff between the size of the window and the max freq of a character
            # is greater than the amount of characters that could be replaced 
            # slide the left pointer
            # And update the frequency of the characters in the count dict 
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1

            result = max(result,r-l+1)

        return result





        


        