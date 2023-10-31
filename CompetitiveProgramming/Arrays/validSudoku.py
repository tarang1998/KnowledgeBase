class Solution:

    # Space Complexity : O(9^2)
    # Time Complexity : O(9^2)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        memRow = {}
        memColumn = {}
        memQuadrant = {}


        for i in range(len(board)):
            for j in range(len(board[0])):

                if(board[i][j] == "."):
                    continue

                else:
                    ele = board[i][j]

                    # Check if the element is present in the same row
                    if((i,ele) in memRow):
                        return False
                    else:
                        memRow[(i,ele)] = 1


                    # Check if the element is present in the same column
                    if((j,ele) in memColumn):
                        return False
                    else:
                        memColumn[(j,ele)] = 1

                    
                    # Check if the element is present in the same quandrant 
                    key = str(i//3) + str(j//3)
                    if((key,ele) in memQuadrant):
                        return False
                    else:
                        memQuadrant[(key,ele)] = 1


        return True


        