class Solution:
    
    def checkIfDigitIsPresentInColumn(self,digit,column,board):
        columnDigits = []
        
        for i in range(0,9):
            columnDigits.append(board[i][column])
                        
        if(str(digit) in columnDigits):
            return True
        else:
            return False
        
    def isValid(self,board,row,column,value):
        
        for i in range(0,9):
            
            if(board[row][i] == value):
                return False
            
            if(board[i][column] == value):
                return False
            
            if(board[3*(row//3) + (i//3)][3*(column//3) + int(i%3)] == value):
                return False
            
        return True
    
        
    def checkIfDigitIsPresentInBlock(self,digit,row,column,board):
        
        blockRowStart = (row//3) * 3 
        blockRowEnd = (row//3) * 3 + 3 
        
        columnRowStart = (column//3) * 3
        columnRowEnd = (column//3) * 3 + 3
        
        blockDigits = []
        
        for i in range(blockRowStart,blockRowEnd):
            for j in range(columnRowStart,columnRowEnd):
                blockDigits.append(board[i][j])
                
        if str(digit) in blockDigits:
            return True
        else:
            return False
        
        
            
        
    
    def findSolution(self,row,column,board):
        
        if(row == 9):
            return True
                
        if(board[row][column] == "." ):
            
            for k in range(1,10):
                
                """
                #check if the digit is present in the row
                if(str(k) in board[row]):
                    continue
                
                #check if the digit is present in the column
                if(self.checkIfDigitIsPresentInColumn(k,column,board)):
                    continue
                

                #check if the digit is present in its block
                if(self.checkIfDigitIsPresentInBlock(k,row,column,board)):
                    continue
                """
                
                if(not self.isValid(board,row,column,str(k))):
                    continue
                     
                #add the digit to the board 
                board[row][column] = str(k)            
            
                #proceed forward with the next block 
                
                result = None 
        
                if(column == 8):
                    result = self.findSolution(row+1,0,board)
                    
                else:
                    result = self.findSolution(row,column+1,board)
                    
                if(result):
                    return True
                    
                else:
                    board[row][column] = "."
                    continue
                        
                            
            return False
            
        else : 
            
            result = None 
        
            if(column == 8):
                result = self.findSolution(row+1,0,board)
                    
            else:
                result = self.findSolution(row,column+1,board)
                
            return result
            

    
    
    def solveSudoku(self, board):
        
        self.findSolution(0,0,board)
        
        return board
        
       
        
                        
                        
                
                
                
       
        