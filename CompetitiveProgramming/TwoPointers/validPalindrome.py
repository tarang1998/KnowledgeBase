class Solution:


    # Time Complexity : O(n)
    # Space Complexity : O(1)

    # We can achieve comlexity of constant space by using 2 pointers
    # One in the beginning and the other at the end to compare the characters
    def isPalindrome(self, s: str) -> bool:

        def isAlphaNumeric(l):

            if ((ord(l) >= 65 and ord(l) <= 90) or 
                (ord(l) >= 97 and ord(l) <= 122)or
                (ord(l) >= 48 and ord(l) <= 57)): 

                return True 

            else:
                return False


        l = 0 
        r = len(s)-1 

        while(l<r):

            # Check if the element at left pointer is alphanumeric
            # If not increment the pointer
            while(l<r and not isAlphaNumeric(s[l])):
                l += 1

            
            # Check if the element at the right pointer is alphanumeric
            # If not decrement the pointer 
            while(r>l and not isAlphaNumeric(s[r])):
                r -= 1

            
            if(s[l].lower() != s[r].lower()):
                return False

            l += 1
            r -= 1 

        return True 

    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def isPalindromeReverseString(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


        