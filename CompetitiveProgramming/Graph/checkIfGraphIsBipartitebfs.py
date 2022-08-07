#https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        #key : vertex 
        #value : 0 for set1, 1 for set2
        belongingToSet = {}
        
        bfsqueue = []
        
        
        for node in range(len(graph)):
            
            if node not in belongingToSet:
                
                belongingToSet[node] = 0 
                
                bfsqueue.append(node)
                
                while(len(bfsqueue)!=0):
                    
                    ele = bfsqueue.pop(0)
                    
                    adjNodes = graph[ele]
                    
                    for adjNode in adjNodes:
                        
                        if adjNode in belongingToSet:
                            if(belongingToSet[adjNode] == belongingToSet[ele]):
                                return False
                        else:
                            if(belongingToSet[ele] == 0):
                                belongingToSet[adjNode] = 1
                                bfsqueue.append(adjNode)
                                
                            else:
                                belongingToSet[adjNode] = 0 
                                bfsqueue.append(adjNode)
                
        return True
                                
                
                
            
        