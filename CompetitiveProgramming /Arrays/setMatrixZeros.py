#https://leetcode.com/problems/set-matrix-zeroes/



class Solution:
    def setZeroes(self, matrix):
        
        noOfRows = len(matrix)
        
        noOfColumns = len(matrix[0])
        
        rowToBeModified = set()
        
        columnToBeModified = set()
        
        for i in range(0,noOfRows):
            
            for j in range(0, noOfColumns):
                
                if(matrix[i][j] == 0):
                
                    rowToBeModified.add(i)
                    columnToBeModified.add(j)
                    
        
        for i in range(0,noOfRows):
                        
            for j in range(0, noOfColumns):
                
                if(i in rowToBeModified or j in columnToBeModified):
                    matrix[i][j] = 0
                    
               
                        
            
            
            
                
                
                
                
                          
                
                
        
        
        
        
        
     
        
        
