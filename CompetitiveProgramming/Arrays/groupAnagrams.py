class Solution:

    # Time Complexity O(m.n)
    # m : no of words
    # n : average length of each word
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs :

            count = [0] * 26

            for c in s :
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)
        
        return res.values()

        