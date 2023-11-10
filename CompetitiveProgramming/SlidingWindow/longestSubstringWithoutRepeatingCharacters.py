class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 

        # Dict to store the characters present in the dict
        cache = {}

        result = 0 

        for r in range(len(s)):

            # A duplicate character is encountered 
            if(s[r] in cache):
                
                # Remove characters from the left side of 
                # the substring till the character s[r] is removed 
                # from the substring 
                while(s[r] in cache):
                    del cache[s[l]]
                    l+=1

            cache[s[r]] = 1
            result = max(result,r-l+1)

        return result

        
        