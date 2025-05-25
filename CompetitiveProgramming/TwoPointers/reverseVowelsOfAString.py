class Solution:

    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def reverseVowels(self, s: str) -> str:

        vowels = {
            "a":1,"A":1, 
            "e":1, "E":1,
            "i":1, "I":1,
            "o":1, "O":1,
            "u":1, "U":1,
            }

        left = 0 
        right = len(s)-1

        s = list(s)

        while left<right:

            if s[left] not in vowels:
                left += 1
                continue
            
            if s[right] not in vowels:
                right -= 1
                continue

            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1 

        return "".join(s)

            






        
        