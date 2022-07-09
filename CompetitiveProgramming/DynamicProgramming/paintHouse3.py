class Solution:
    
    
    MAX_COST = float('inf')
    
    
    
            
    def findMinCost(self,houses,cost,targetNeighbourhoodCount,currHouseIndex,neighbourhoodCount,prevHouseColor,memo):


        #Check if all the houses have been traversed
        if(currHouseIndex == len(houses)):
            
            #Check if the target neighbourhood has been reached
            if(targetNeighbourhoodCount == neighbourhoodCount):
                return 0 
            else:
                return self.MAX_COST
                
        
        #Check if neighbourhoodCount has exceeded the target 
        if(neighbourhoodCount>targetNeighbourhoodCount):
            return self.MAX_COST
        
        if(memo[currHouseIndex][neighbourhoodCount][prevHouseColor] != None ):
            
          
            return memo[currHouseIndex][neighbourhoodCount][prevHouseColor]
            
                    
            
        minCost = self.MAX_COST
                     
        
        #Check if the house is painted
        if(houses[currHouseIndex] == 0):
            
            #The house isn't painted 
            #Iterate through all the colors 
            totalColors = len(cost[0])
            
            for i in range(1,totalColors+1):
                currCost = 0 
                if(prevHouseColor == i):
                    currCost = cost[currHouseIndex][i-1] + self.findMinCost(houses,cost,targetNeighbourhoodCount,currHouseIndex + 1,neighbourhoodCount,prevHouseColor,memo)
                else:
                    currCost = cost[currHouseIndex][i-1] + self.findMinCost(houses,cost,targetNeighbourhoodCount,currHouseIndex + 1,neighbourhoodCount+1,i,memo)

                minCost = min(minCost,currCost)
                    
                    
            
        else: 
            
            #The house is painted 
            #Proceed forward to the next house
            
            #Check the previous house color to update the neighbourhood count 
            if(prevHouseColor == houses[currHouseIndex]):
                minCost = self.findMinCost(houses,cost,targetNeighbourhoodCount,currHouseIndex + 1,neighbourhoodCount,houses[currHouseIndex],memo)
                
                
            else:
                minCost = self.findMinCost(houses,cost,targetNeighbourhoodCount,currHouseIndex + 1,neighbourhoodCount + 1,houses[currHouseIndex],memo)
                
                
        memo[currHouseIndex][neighbourhoodCount][prevHouseColor] = minCost
    
        #print(currHouseIndex,neighbourhoodCount,prevHouseColor,houses[currHouseIndex],minCost)
        return  memo[currHouseIndex][neighbourhoodCount][prevHouseColor]
            
            
            
        
        
        
    
    def minCost(self, houses, cost, m: int, n: int, target: int):
        
        memo = []
        
        for i in range(0,m):
            memo.append([])
            for j in range(0,target+1):
                memo[i].append([])
                for k in range(0,n+1):
                    memo[i][j].append(None)
                
        
        answer = self.findMinCost(houses,cost,target,0,0,0,memo)
        
        #print(memo)
        
        if (answer == self.MAX_COST):
            return -1
        else:
            return answer
        