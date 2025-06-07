import heapq
from collections import Counter


class Solution:
    def robotWithString(self, s: str) -> str:

        count = Counter(s)
        q = list(count.keys())
        heapq.heapify(q)

        stack = []
        result = ""

        def getLeastCharacter():
            while q:
                minChar = q[0]
                if count[minChar] == 0:
                    heapq.heappop(q)
                else:
                    return minChar
                
        for ch in s:
            stack.append(ch)
            count[ch] -=1
            minChar = getLeastCharacter()
            while len(stack)>0 and minChar and stack[-1] <= minChar:
                result += stack.pop()   
        return result + "".join(stack[::-1])

                
            
            