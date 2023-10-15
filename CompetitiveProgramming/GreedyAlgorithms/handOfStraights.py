import heapq

class Solution:

    # Time Complexity : O(logn*n)
    # The idea is that whenever a set has to be created 
    # the minimum value is taken from the list and then other consecutive elements are searched 
    # If Consecutive elements are not found then the development of the set is not possible 
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool: 

        # Check if is possible to form groups with the given size 
        if(len(hand) % groupSize):
            return False 

        #Count the occurence of each card 
        count = {}

        for card in hand:
            if card in count:
                count[card] += 1
            else:
                count[card] = 1


        
        #Create a min heap from the given elements 
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while(len(minHeap) != 0 ):


            # Retrieve the min element from the heap
            minEle = minHeap[0]

            # Loop through the elements to create the set of group size
            for i in range(minEle , minEle + groupSize):

                if i not in count:
                    return False

                count[i] -= 1

                if (count[i] == 0):
                    # If the count of an element goes to zero which is not the minimum card
                    # Then the set cannot be formed 
                    # As there would be an element before it and hence a consecutive sequence cannot be formed
                    if(i != minHeap[0]):
                        return False

                    heapq.heappop(minHeap)
                

        return True 



            

        

        





        






        