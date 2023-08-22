class Solution:

    count = 0 

    def checkPalindrome(self,s,l,r):

        while l>=0 and r<len(s) and s[l]==s[r]:
            self.count += 1
            l -= 1
            r += 1 

    def countSubstrings(self, s: str) -> int:

        for i in range(len(s)):

            #Check for odd palindromes
            self.checkPalindrome(s,i,i)

            #Check for even palindromes
            self.checkPalindrome(s,i,i+1)

        return self.count