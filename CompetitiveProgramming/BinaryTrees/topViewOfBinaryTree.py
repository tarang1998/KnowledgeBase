    #User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    maxHorizontalDistance = 0
    minHorizontalDistance = 0 
    
    solution = {}
    
    
    def parseTree(self,node,level,horizontalDistance):
        
        if(node == None):
            return
        
        if(horizontalDistance not in self.solution):
            
            self.solution[horizontalDistance] = (level,node.data)
            
            if(horizontalDistance > self.maxHorizontalDistance):
                self.maxHorizontalDistance = horizontalDistance
                
            if(horizontalDistance < self.minHorizontalDistance):
                self.minHorizontalDistance = horizontalDistance
            
        else:
            
            hlevel = self.solution[horizontalDistance][0]
            
            if(level < hlevel):
                
                self.solution[horizontalDistance] = (level,node.data)
              
        self.parseTree(node.left,level+1,horizontalDistance - 1 )
        
        self.parseTree(node.right, level + 1, horizontalDistance + 1)
        
        
        return
        
        
        
       
        
        
        
        
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        self.maxHorizontalDistance = 0
        self.minHorizontalDistance = 0
        
        self.solution = {}
        
        
        self.parseTree(root,0,0)
        
        arr = []
        
        for i in range(self.minHorizontalDistance, self.maxHorizontalDistance + 1):
            
            arr.append(self.solution[i][1])
            
            
        return arr
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob= Solution()
        
        res = ob.topView(root)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends