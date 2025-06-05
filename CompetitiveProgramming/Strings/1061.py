from collections import defaultdict

class Solution:

    # Using Disjoint Set Union (aka union‐find)
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                return x
            
            if parent[x] != x:
                return find(parent[x])
            else:
                return x
        
        def union(c1,c2):

            c1 = find(c1)
            c2 = find(c2)

            if c1>c2:
                parent[c1] = c2
            else:
                parent[c2] = c1

        for c1,c2 in zip(s1,s2):
            union(c1,c2)

        result = ""
        for c in baseStr:
            result += find(c)
        return result
            



    def smallestEquivalentString1(self, s1: str, s2: str, baseStr: str) -> str:
        sets = []
        for c1,c2 in zip(s1,s2):
            setFound = False
            c1Set = None 
            c2Set = None 
            for cset in sets:
                if c1 in cset and c2 in cset:
                    cset.update([c1,c2])
                    setFound = True
                    break
                if c1 in cset:
                    setFound = True
                    c1Set = cset
                if c2 in cset:
                    setFound = True
                    c2Set = cset
    
            if not setFound:
                sets.append({c1,c2})

            if c1Set and c2Set:
                sets.remove(c1Set)
                sets.remove(c2Set)
                merge = c1Set.union(c2Set)
                sets.append(merge)
            elif c1Set:
                c1Set.update([c1,c2])
            elif c2Set:
                c2Set.update([c1,c2])

        print(sets)
        result = ""
        for i in range(len(baseStr)):
            c = baseStr[i]
            setFound = False
            for cset in sets:
                if c in cset:
                    setFound = True
                    result += min(cset)
                    break
            if not setFound:
                result += c
        return result
            

        