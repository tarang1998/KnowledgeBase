class Solution:

    # Greedy Solution
    # Time Complexity : O(n)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        startIndex = 0 
        total = 0 

        # A round trip is not possible if 
        # the cost of travel is more than the gas available
        if(sum(cost) > sum(gas)):
            return -1

        # If the solution exist it is gauranteed to be a unique one 
        for i in range(len(gas)):

            total += gas[i] - cost[i]

            # If the total is less than zero 
            # then startIndex cant be the starting point
            # to travel around the circuit once 
            if(total < 0):
                total = 0 
                startIndex = i + 1

        return startIndex


        

    # Recursive Solution
    # Time Limit Exceeded
    # With Caching Memory Limit Exceeded 
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:

        # No of stations 
        n = len(gas)

        # Figuring out the starting poi nt
        # Saving all the possible starting Indexes in an array 
        # Starting at the point which has gas available to travel to the next station 
        startPositions = []

        # Saving the already computed combinations of (gasLeft, index)
        # mem = {}

        for i in range(n):
            t = gas[i]-cost[i] 
            if(t >= 0 ):
                startPositions.append(i)

        if(len(startPositions) == 0 ):
            return -1

        for startIndex in startPositions :


            # Going through all the stations
            gasLeft = gas[startIndex]-cost[startIndex] 

            currentIndex = (startIndex + 1) % n
            
            def parse(currentIndex,gasLeft):


                if(currentIndex == startIndex):
                    return startIndex

                # if((currentIndex,gasLeft) in mem):
                #     return mem[(currentIndex,gasLeft)]

                gasLeft += gas[currentIndex] - cost[currentIndex]

                if(gasLeft < 0):
                    # mem[(currentIndex,gasLeft)] = - 1
                    return -1 

                # mem[(currentIndex,gasLeft)] = 
                return parse((currentIndex + 1)%n, gasLeft)

                # return mem[(currentIndex,gasLeft)]

            result = parse(currentIndex, gasLeft)

            if(result != -1 ):
                return result
            
        return -1



        




        