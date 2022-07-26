# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    
    solution = {}
    
    maxHorizontalDistance = 0 
    
    minHorizontalDistance = 0 
    
    def parseTree(self,node,level,horizontalDistance):
        
        if(node == None):
            return 
        
       
        
        if(horizontalDistance not in self.solution):
            
            self.solution[horizontalDistance] = [(level,node.val)]
            
            if(self.maxHorizontalDistance < horizontalDistance):
                self.maxHorizontalDistance = horizontalDistance
                
            if(self.minHorizontalDistance > horizontalDistance):
                self.minHorizontalDistance = horizontalDistance
            
        else:
            
            arr =  self.solution[horizontalDistance]
            
            
            for i in range(len(arr)):
                
                #if levels are equal
                if(level == arr[i][0]):
                    
                    val = arr[i][1]
                    
                    if(val < node.val):
                        pass
                    else:
                        arr.insert(i,(level,node.val))
                        break

                elif(level < arr[i][0]):
                    
                    arr.insert(i,(level,node.val))
                    break
                    
                
                if(i == len(arr)-1):

                    arr.append((level,node.val))
        
        self.parseTree(node.left,level+1,horizontalDistance-1)
        
        self.parseTree(node.right,level+1,horizontalDistance + 1)
                    
        return
                    
        
            
            

    def verticalTraversal(self, root):
        
        self.solution = {}
        
        self.maxHorizontalDistance = 0 
        
        self.minHorizontalDistance = 0 
        
        self.parseTree(root,0,0)
        
        result = []
        
        
        for i in range(self.minHorizontalDistance, self.maxHorizontalDistance + 1):
            
            arr = self.solution[i]
            
            levelele = []
            
            for j in range(len(arr)):
                levelele.append(arr[j][1])
            
            result.append(levelele)
            
        return result 
            
            
        
        