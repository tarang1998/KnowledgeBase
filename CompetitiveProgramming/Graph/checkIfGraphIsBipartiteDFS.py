# https://leetcode.com/problems/is-graph-bipartite/


class Solution:
    
    belongingSet = None

    
    def parseGraph(self,node,graph):
        adjNodes = graph[node]
        
        for adjNode in adjNodes:
            
            if(adjNode in self.belongingSet):
                
                if(self.belongingSet[adjNode] == self.belongingSet[node]):
                    
                    return False
                                 
            else:
                result = None
                if(self.belongingSet[node] == 0 ):
                    self.belongingSet[adjNode] = 1 
                    result = self.parseGraph(adjNode,graph)
                else:
                    self.belongingSet[adjNode] = 0
                    result =  self.parseGraph(adjNode,graph)
                if(not result):
                    return result
                    
        return True
        
                
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        self.belongingSet = {}
        
        for node in range(len(graph)):

            if (node not in self.belongingSet):
                
                self.belongingSet[node] = 0
                result = self.parseGraph(node,graph)
                if(not result):
                    return False
                
        return True 
                
        

    
  