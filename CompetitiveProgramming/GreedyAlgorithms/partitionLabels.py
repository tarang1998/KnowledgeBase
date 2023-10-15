class Solution:

    # Time Complexity : O(n)
    def partitionLabels(self,s: str) -> List[int]:

        # Create a dictionary to store the last position of the ocurrence of the letter
        letterPos = {}

        for index in range(len(s)):

            letter = s[index]
            letterPos[letter] = index

        
        # Calculate all the partitions that are possible
        partitionSize = []

        size = 0
        end = 0

        for index in range(len(s)):

            letter = s[index]
            lastIndexPosition = letterPos[letter]

            if( end < lastIndexPosition):
                end = lastIndexPosition

            
            size += 1

            if(index == end):
                partitionSize.append(size)
                size = 0 

        return partitionSize



            

            



    
    def partitionLabels1(self, s: str) -> List[int]:

        letterPos = {}

        partitionIndex = {}

        def removeIndexes(l,r):
            for i in range(l,r):
                if i in partitionIndex :
                    del partitionIndex[i]

        # Loop through all the letters in the string
        for index in range(len(s)):

            letter = s[index]

            if letter in letterPos:

                # Getting the previous index of the occurence of the letter
                prevIndex = letterPos[letter]

                # We cannot form partition at any index 
                # between the prevIndex and the current Index
                # Removing all the indexes from the partitionIndex dict
                removeIndexes(prevIndex,index)


            else:
                
                letterPos[letter] = index
            
            partitionIndex[index] = 1

        partitionSizes = []

        # We got the indexes where the partition can be created 
        # Finding the partition sizes

        prevIndex = -1

        for index in partitionIndex.keys():

            partitionSizes.append(index - prevIndex )

            prevIndex = index 

        return partitionSizes



        