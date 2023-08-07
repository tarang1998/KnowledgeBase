"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def __init__(self):
        # Dictionary holding the all the visited nodes of the LL as keys 
        # And corresponding copied nodes for the new LL as values 
        self.processedNodeRecord = {}


    # Acts like a recursive function 
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if(head ==  None):
            return None 

        # If node is already processed returning it 
        if(head in self.processedNodeRecord):
            return self.processedNodeRecord[head]

        # Creating the corresponding Node
        node = Node(head.val,None,None)

        self.processedNodeRecord[head] = node 

        node.next = self.copyRandomList(head.next)

        node.random = self.copyRandomList(head.random)

        return node 
