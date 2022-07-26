
class Solution:
    
    def parseTree(self,node,level,solution):
        
        if(node == None):
            return
        
        if level > len(solution):
            solution.append([])
            
        solution[level-1].append(node.val)
        
        self.parseTree(node.left,level + 1, solution)

        
        self.parseTree(node.right,level + 1,solution)
        
        
        
            
        
    
    def levelOrder(self, root):
        
        solution = []
        
        self.parseTree(root,1,solution)
        
        return solution
        
        
        
        