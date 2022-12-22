from collections import defaultdict

class Graph:

    def __init__(self,vertexCount):
        self.vertexCount = vertexCount
        self.adjVertex = defaultdict(list)

    def addEdge(self,u,v):
        self.adjVertex[u].append(v)
        self.adjVertex[v].append(u)




class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = Graph(n)


        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph.addEdge(u,v)

        stack = []
        visited = [0] * n

        stack.append(source)
        visited[source] = 1

        while(len(stack)!=0):
            
            node = stack.pop()

            if(node == destination):
                return True 

            for neighbour in graph.adjVertex[node]:
                if (visited[neighbour] == 0):
                    visited[neighbour] = 1
                    stack.insert(0,neighbour)

        return False

    


        



    def validPathDFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def dfs(node,vertexEdge,destination):

            if(node == destination):
                return True

            vertexEdge[node][0] = 1

            for vertex in vertexEdge[node][1]:

                if(vertexEdge[vertex][0] == 1):
                    continue 
            
                if(dfs(vertex,vertexEdge,destination)):
                    return True

            return False

            if(len(edges) == 0):
                if(source == destination):
                    return True 
                else:
                    return False

        
        if(len(edges) == 0):
            if(source == destination):
                return True 
            else:
                return False

        #key : vertex
        #Value : [visitedStatus,[adjacentVertexes]]
        vertexEdge = {}


        for edge in edges:
            edge1 = edge[0]
            edge2 = edge[1]

            if edge1 in vertexEdge:
                vertexEdge[edge1][1].append(edge2)
            else:
                vertexEdge[edge1] = [0,[edge2]]

            if edge2 in vertexEdge:
                vertexEdge[edge2][1].append(edge1)
            else:
                vertexEdge[edge2] = [0,[edge1]]


        for vertex in vertexEdge[source][1]:

            if(dfs(vertex,vertexEdge,destination)):
                return True
        
        return False







