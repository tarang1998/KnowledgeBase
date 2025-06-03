class Solution:
    
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        if len(initialBoxes) == 0:
            return 0 

        boxKeys = {}
        boxesToOpen = initialBoxes 
        total = 0 

        while(boxesToOpen):
            n = len(boxesToOpen)
            noBoxIsOpened = True
            tmp = []
            for i in range(n):
                box = boxesToOpen[i]
                # Check if box can be opened 
                if status[box] == 1 or box in boxKeys:
                    noBoxIsOpened = False
                    total += candies[box]
                    tmp.extend(containedBoxes[box])
                    for key in keys[box]:
                        boxKeys[key] = 1
                else:
                    tmp.append(box)
            boxesToOpen = tmp
            if(noBoxIsOpened):
                return total
        return total