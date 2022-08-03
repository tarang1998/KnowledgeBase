class Solution:

  visited = {}

  #(Current Node, Previous Node)
  queue = []

  def checkForCycle(self,node,graph):
    
    self.visited[node] = 1
    self.queue.append((node,-1))

    while(len(self.queue) != 0):
      
      nodes = self.queue.pop(0)

      currentNode = nodes[0]
    
      parentNode = nodes[1]
      currentNodeAdjNodes = graph[currentNode]
      for adjNode in currentNodeAdjNodes:
        if(adjNode not in self.visited):        
          self.visited[adjNode] = 1
          self.queue.append((adjNode,currentNode))
        else:
          if(adjNode != parentNode):
            return True
            
    return False

    
      

  def isGraphCyclic(self,graph):

    self.visited = {}

    self.queue = []

    #Solution doesnt work for 2 nodes 
    #With edges = 0->1 and 1->0
    if(len(graph) == 2):

      key1 = list(graph.keys())[0]

      key2 = list(graph.keys())[1]

      if(len(graph[key1]) == 1 and graph[key1][0] == key2 and len(graph[key1]) == 1 and graph[key2][0] == key1):
        return True

  
      
      
    
    
    for node,adjNodes in graph.items():

      if(node not in self.visited):

        result = self.checkForCycle(node,graph)
        if(result):
          return True

    return False 

        

    





solution = Solution()

graph1 = {0:[1,5,7],1:[0,7],2:[4],4:[2,6],5:[0],6:[4],7:[0,1]}

result1 = solution.isGraphCyclic(graph1)
print('Graph1 : ',graph1)
print('Graph1 is cyclic : ',result1)

graph2 = {1:[2,3],2:[1,4],3:[1,4],4:[2,3]}

result2 = solution.isGraphCyclic(graph2)
print('Graph2 : ',graph2)
print('Graph2 is cyclic : ',result2)

graph3 = {1:[2,3],2:[1,4],3:[1,5],4:[2],5:[3]}

result3 = solution.isGraphCyclic(graph3)
print('Graph3 : ',graph3)
print('Graph3 is cyclic : ',result3)

graph4 = {1:[2,3],2:[1,3],3:[1,2]}

result4 = solution.isGraphCyclic(graph4)
print('Graph4 : ',graph4)
print('Graph4 is cyclic : ',result4)

graph5 = {0:[1],1:[0]}

result5 =  solution.isGraphCyclic(graph5)
print('Graph5 : ',graph5)
print('Graph5 is cyclic : ',result5)

graph6 = {1:[],2:[]}

result6 = solution.isGraphCyclic(graph6)
print('Graph6 : ',graph6)
print('Graph6 is cyclic : ',result6)

graph7 = {1:[1]}

result7 = solution.isGraphCyclic(graph7)
print('Graph7 : ',graph7)
print('Graph7 is cyclic ',result7)




