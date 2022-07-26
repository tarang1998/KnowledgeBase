#https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        
        output = []
        
        for i in range(1,numRows+1):
            
            if(i == 1):
                output.append([1])
                
            elif(i == 2):
                output.append([1,1])
                
            else:
                previousRow = output[i-2]
                
                nextRow = [1]
                
                for j in range(0,len(previousRow)-1):
                    
                    nextRow.append(previousRow[j]+previousRow[j+1])
                    
                nextRow.append(1)
                
                output.append(nextRow)
                
        return output
                    
            