
class Solution:


    def findPalindrome(self,s,l,r):
        # Check if the string is an palindrome 
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:

        result = ""

        for i in range(len(s)):

            # 1> Finding the occurence of an odd palindrome number : i being the center of the palindrome
            # 2> Finding the occurence of an even palindrome number : i and i+1 being the elements of the palindrome
            result = max([result,self.findPalindrome(s,i,i),self.findPalindrome(s,i,i+1)],key=len)

        return result


        

