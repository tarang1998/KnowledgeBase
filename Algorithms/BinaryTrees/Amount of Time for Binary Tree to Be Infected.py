# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:


    # Time Complexity : O(n)
    # Space Complexity : O(n)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        # Create an undirected graph from the given tree using depth first search
        graph = defaultdict(list)

        def dfs(node):
            if not node:
                return

            if node.left:
                graph[node.left.val].append(node.val)
                graph[node.val].append(node.left.val)

            if node.right:
                graph[node.right.val].append(node.val)
                graph[node.val].append(node.right.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)


        # Process each of the nodes from the starting node using Breadth First Search to calculate the time taken to infect the entire tree 
        visited = {}
        queue = [start]
        totalTime = -1

        while(queue):

            totalTime += 1 

            n = len(queue)

            # Parse through each element present in the queue
            for i in range(n):
                ele = queue.pop()
                visited[ele] = 1

                # Insert the adjacent nodes in the queue in case they are not visited 
                for j in graph[ele]:
                    if j not in visited:
                        queue.insert(0,j)

        return totalTime 