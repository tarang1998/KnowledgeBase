from collections import Counter

class Solution:
    # Time Complexity : O(n)
    def isAnagram(self,s: str, t: str) -> bool:
        # Anagrams must be the same length
        if len(s) != len(t):
            return False

        # Use Counter to count frequency of each character in both strings
        return Counter(s) == Counter(t)
        