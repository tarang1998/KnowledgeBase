class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        # Check if any child has 2 parents 
        # If that is the case then it is not a valid binary tree
        childNodes = {}

        # Checking the left child array
        for node in leftChild:
            if node == -1:
                continue
            if node in childNodes:
                return False
            else:
                childNodes[node] =  1

        # Checking the right child array
        for node in rightChild:
            if node == -1:
                continue
            if node in childNodes:
                return False
            else:
                childNodes[node] =  1




        # Find the root of the tree
        # The root node would be the one that is not present 
        # in the dictionary of the childNodes

        # - If the structure has two roots then it is invalid
        # - If the struture has no roots the structure is invalid
        # - If there are multiple structures in the given data with separate roots 
        #   it is invalid

        ##  There might be a case when there are multiple structures present but only one 
        ##  root is captured as the other components could have a cyclic structure
        roots = []

        for node in range(n):

            if node not in childNodes:
                roots.append(node)

        if(len(roots) == 0 or len(roots) > 1):
            return False

        root = roots[0]

        # Check if the structure with the given root has a cycle
        visited = {}

        def recurse(index):

            if(index == - 1):
                return True

            if(index in visited):
                return False

            visited[index] = 1

            left = leftChild[index]
            
            right = rightChild[index]

            return (recurse(left) and recurse(right))

        
        res =  recurse(root)

        # Check for the possibility that there could be multiple components
        # in which case those nodes wont be visited
        if(len(visited.keys()) == n and res):
            return True
        else:
            return False
        

       

        