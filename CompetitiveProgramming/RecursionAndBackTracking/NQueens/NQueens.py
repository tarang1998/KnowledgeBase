class Solution(object):
    
    allSolutions = []
    
    def checkIfPositionIsSafe(self,n,row,column,solutionMatrix):
        
        for i in range(0,column):
            #check if there are any elements set in the row to the left
            if(solutionMatrix[row][i] == 1):
                return False
               
          
        #check if any elements are set in the upper diagonal in the left side 
        temp_row = row -1
        temp_column = column - 1
        while(temp_row > -1 and temp_column > -1):
            if(solutionMatrix[temp_row][temp_column] == 1):
                return False
            temp_row -= 1
            temp_column -= 1
            
        #check if any elements are set in the lower diagonal in the left side 
        temp_row = row + 1
        temp_column = column - 1 
        while(temp_row < n and temp_column > -1):
            if(solutionMatrix[temp_row][temp_column] == 1):
                return False
            temp_row += 1
            temp_column -= 1
                
            
        return True
    

    
    
    
    def convertOutput(self,n,solutionMatrix):
        
        solution = []
        
        for i in range(0,n):
            tempString = ""
            for j in range(0,n):
                if(solutionMatrix[i][j] == 1):
                    tempString = tempString + 'Q'
                else :
                    tempString = tempString + '.'
            solution.append(tempString)
            
        return solution
            

            
            
    
    def findCombinations(self, n, column, solutionMatrix):
        
        #check if all the columns are filled
        if(column >= n):
           
            self.allSolutions.append(self.convertOutput(n,solutionMatrix))
            return
            
        #Try placing the queens in each row 
        if(column == 0 ):
            
            #The Queens can be safely placed in each of the rows 
            #No need to perform any additional checks 
            
            for i in range(0,n):
                
                solutionMatrix[i][0] = 1
                
                self.findCombinations(n,1,solutionMatrix)
                
                solutionMatrix[i][0] = 0 
                
        else: 
            
            #Placement checks needs to be performed before placement
            
            for i in range(0,n):
                
                isPositionSafe = self.checkIfPositionIsSafe(n,i,column,solutionMatrix)

                if(isPositionSafe):
                    
                    solutionMatrix[i][column] = 1
                    
                    self.findCombinations(n,column+1,solutionMatrix)
                    
                    solutionMatrix[i][column] = 0 
                    
                
                
                
                
            
            
            
            
    
    
    def solveNQueens(self, n):
        
        solutionMatrix = []
        
        for i in range(0,n):
            row = []
            
            for j in range(0,n):
                row.append(0)
                
            solutionMatrix.append(row)
            
        self.findCombinations(n,0,solutionMatrix)
        
        temp = self.allSolutions.copy()
        
        self.allSolutions.clear()
        
        return temp
        
        
            
                
        
        
        
        
        
        
       
        