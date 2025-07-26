# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # Time Complexity: O(N + M)
    # Space Complexity : O(N)
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Base case: if the input node is None, return None to handle empty graph
        if not node:
            return None

        # Dictionary to map original nodes to their cloned counterparts
        old_to_new = {}

        def dfs(n: 'Node') -> 'Node':
            # If this node is already cloned, return its clone to avoid cycles
            if n in old_to_new:
                return old_to_new[n]

            # Create new node with the same value
            clone = Node(n.val)
            old_to_new[n] = clone  # Store mapping before exploring neighbors

            # Recursively clone each neighbor
            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        # Kickoff DFS cloning from the given start node
        return dfs(node)
