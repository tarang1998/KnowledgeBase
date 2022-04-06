#https://leetcode.com/problems/set-matrix-zeroes/



class Solution:


    #Time complexity : O(mn)
    #Space Complexity : O(m+n)
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

    #Optimizing space utilization
    #Time complexity : O(mn)
    #Space Complexity : O(1)
    def setZeroApproach2(self,matrix):

        noOfRows = len(matrix)

        noOfColumns = len(matrix[0])

        doesFirstColumnNeedToBeSetToZero =  False

        #Assuming the first cell of every row and column to be a flag
        #In this case the flag for the first row and the first column would coincide
        #Assuming matrix[0][0] as the flag for the first row
        #Flag for the first column would be saved in a variable

        for i in range(0,noOfRows):

            for j in range(0,noOfColumns):

                if(matrix[i][j]==0):

                    if(j == 0):
                        doesFirstColumnNeedToBeSetToZero = True
                        matrix[i][0]=0
                    

                    else:
                        matrix[i][0]=0
                        matrix[0][j]=0

        #Setting the rows of the matrix to 0
        #Ignoring the first row of the matrix 
        #As it acts like a flag for the columns 
        for i in range(1,noOfRows):

            if(matrix[i][0]==0):

                for j in range(0,noOfColumns):

                    matrix[i][j] = 0

        
        #setting the columns of the matrix to 0
        #Ignoring the first column
        for j in range(1,noOfColumns):


            if(matrix[0][j] == 0):

                for i in range(0,noOfRows):

                    matrix[i][j] = 0   

        #Checking if the first row needs to be set to 0 
        if(matrix[0][0] == 0):
            for j in range(1,noOfColumns):
                matrix[0][j] = 0 

        #Checking if the first column needs to be set to 0 
        if(doesFirstColumnNeedToBeSetToZero):
            for i in range(0,noOfRows):
                matrix[i][0] = 0




               
                        
            
            
            
                
                
                
                
                          
                
                
        
        
        
        
        
     
        
        
