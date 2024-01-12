
class Solution: 
    # Time Complexity : O(n), where n is the length of the string
    # Space Compexity : O(1)
    def halvesAreAlike(self, s: str) -> bool:

        length = len(s)

        s1 = s[:length//2]
        s2 = s[length//2:]

        s1vowelCount = 0
        s2vowelCount = 0

        
        vowels = {'a':1,'e':1,'i':1,'o':1,'u':1,'A':1,'E':1,'I':1,'O':1,'U':1}
        
        for i in range(len(s1)):

            c1 = s1[i]
            c2 = s2[i]

            if c1 in vowels:
                s1vowelCount += 1
            if c2 in vowels:
                s2vowelCount += 1

        if s1vowelCount == s2vowelCount:
            return True 
        else:
            return False

            

            
