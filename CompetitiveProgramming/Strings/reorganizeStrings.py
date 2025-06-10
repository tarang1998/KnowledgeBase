import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        maxFrequency = 1 
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
                maxFrequency = max(maxFrequency,count[ch])
            else:
                count[ch] = 1

        if maxFrequency == 1:
            return s
        
        # no of even spaces in a string : (len(s)+1)/2
        if maxFrequency > (n+1)//2:
            return ""

        q = []
        for key,value in count.items():
            q.append((-value,key))

        heapq.heapify(q)
        temp = []
        while q:
            f = heapq.heappop(q)
            temp.extend([f[1]]*abs(f[0]))
        result = ['*']*len(s)
        
        c = 0 
        for i in range(0,n,2):
            result[i] = temp[c]
            c+=1

        for i in range(1,n,2):
            result[i] = temp[c]
            c+=1 

        return "".join(result)


        
            

        