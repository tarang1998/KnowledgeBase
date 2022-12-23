from collections import defaultdict

class Solution:

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        # Count of the no of nodes in the subtree with root i
        count = [1] * n

        # The sum of the distances from the root to all nodes in the subtree
        res = [0] * n

        visited = [0] * n

        adjVertex = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]
            adjVertex[u].append(v)
            adjVertex[v].append(u)

        def dfs(root):
            visited[root] = 1
            for neighbour in adjVertex[root]:
                if(visited[neighbour] == 0 ):
                    dfs(neighbour)
                    count[root] += count[neighbour]
                    res[root] += res[neighbour] + count[neighbour]
        
        def dfs2(root):
            visited[root] = 1
            for neighbour in adjVertex[root]:
                if(visited[neighbour] == 0):
                    res[neighbour] = res[root] - count[neighbour] + (n- count[neighbour])
                    dfs2(neighbour)


        dfs(0)

        visited = [0] * n

        dfs2(0)

        return res


    def sumOfDistancesInTreeDFSNTimes(self, n: int, edges: List[List[int]]) -> List[int]:

        distanceMatrix = []

        for i in range(n):
            arr = []
            for j in range(n):
                arr.append(float('inf'))
            distanceMatrix.append(arr)

        adjVertex = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]

            distanceMatrix[u][v] = 1
            distanceMatrix[v][u] = 1

            adjVertex[u].append(v)
            adjVertex[v].append(u)

        def dfs(node,parent,visited,distanceFromParent):

            visited[node] = 1
            distanceMatrix[node][parent] = distanceFromParent
            distanceMatrix[parent][node] = distanceFromParent

            for neighbour in adjVertex[node]:
                if(visited[neighbour] == 0):
                    dfs(neighbour,parent,visited,distanceFromParent+1)

        
        for vertex in range(n):

            visited = [0]*n 
            visited[vertex] = 1

            for neighbour in adjVertex[vertex]:
                dfs(neighbour,vertex,visited,1)

        result = []

        for i in range(n):
            total = 0 
            for j in range(n):
                if(i!=j):
                    total += distanceMatrix[i][j]
            result.append(total)

        return result








                