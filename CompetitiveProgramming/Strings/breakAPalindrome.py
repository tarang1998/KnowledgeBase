# https://leetcode.com/problems/break-a-palindrome/

class Solution:

    def checkIfPalindrome(self, word):
        if(word == word[::-1]):
            return True
        else:
            return False


    def breakPalindrome(self, palindrome: str) -> str:

        if(len(palindrome) == 1):
            return ""

        for i in range(len(palindrome)):
            if(palindrome[i] != "a"):
                if(self.checkIfPalindrome(palindrome[:i] + "a" + palindrome[i+1:])):
                    continue
                return palindrome[:i] + "a" + palindrome[i+1:]

        return palindrome[:len(palindrome)-1] + "b"   

