#https://leetcode.com/problems/minimum-number-of-refueling-stops/

class Solution:
    
    #Complexity : O(N^2)
    def minRefuelStops2(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        #fuel[i][j] : It represnts the maximum distance reached if stopped at
        #j fuel stops from i stops
        fuel = []
       
        for i in range(0,len(stations)+1):
            fuel.append([])
            for j in range(0,len(stations)+1):
                fuel[i].append(0)
        
        #Case where the car didnt stop at any gas station
        for i in range(0,len(stations)+1):
            fuel[i][0] = startFuel
            
        for i in range(1,len(stations)+1):

            for j in range(1,i+1):

                # The case where fuel isnt picked up from the current station
        
                fuel[i][j] = fuel[i-1][j]
                
                # Case where fuel is picked up from the current stations
                if(fuel[i-1][j-1] >= stations[i-1][0]):
                    fuel[i][j] = max(fuel[i][j] , fuel[i-1][j-1] + stations[i-1][1])
                    
                #print(i,j,fuel[i])
                    
                
        for j in range(0,len(stations)+1):
            
            if(fuel[len(stations)][j] >= target):
                return j
            
        return -1

    # Complexity : O(NlogN)  
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        fuelStations = []
        
        
        fuelStops = 0 
        
        carPosition = 0 
        carFuel = startFuel
        
        stations.append((target,float('inf')))
        
        for stationPosition, fuel in stations:
            
            carFuel -= (stationPosition - carPosition)
            
            while(len(fuelStations)!= 0 and carFuel < 0):
                carFuel += -heapq.heappop(fuelStations)
                fuelStops += 1
            
            if(carFuel < 0 ):
                return -1
            
            heapq.heappush(fuelStations,-fuel)
            carPosition = stationPosition
            
        return fuelStops
        
                
        
            
            
            