
from collections import deque

class Solution:
    def findOrder(words):

        adj = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            minLength  = min(len(word1),len(word2))

            if word1[:minLength] == word2[:minLength] and len(word1)>len(word2):
                return ""

            for j in range(minLength):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break


        # Mark as False if node is selected and processed (it has no outbound edges)
        # Mark as True if node is selected and is in the current path (it had outbound edges yet to be traversed)
        visited = {}
        stack = [] 

        # Return True in presence of a cycle 
        def dfs(node):

            if node in visited:
                return visited[node]

            visited[node] = True

            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True

            visited[node] = False 

            stack.insert(0,node)

        characters = list(adj.keys())
        
        for c in characters:
            if dfs(c):
                return ""
            
        return "".join(stack)



    def foreignDictionary(self, words):
        adj = {}
        indegree = {}
        for word in words:
            for c in word:
                adj[c] = set()
                indegree[c] = 0 
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minLen = min(len(word1),len(word2))
            if len(word1)>len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
        
        q = deque([c for c in indegree if indegree[c] == 0])
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(result) != len(indegree):
            return ""
        return "".join(result)
        
            




