from collections import defaultdict

class Solution:

    # Using DFS
    # Time Complexity : O(E+V)
    # Space Complexity : O(E+V)
    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preRequisiteMapping = defaultdict(list)

        visitedPathNodes = {}

        for course,prerequisite in prerequisites:
            preRequisiteMapping[course].append(prerequisite)

        def dfs(course):

            if course in visitedPathNodes:
                return False
            
            if preRequisiteMapping[course] == []:
                return True

            visitedPathNodes[course] = 1 
            for prerequisite in preRequisiteMapping[course]:
                if not dfs(prerequisite):
                    return False
            del visitedPathNodes[course]
            preRequisiteMapping[course] = []
            return True 


        for n in range(numCourses):
            if not dfs(n):
                return False
        return True 

    # Using Topological Sort / Kahn's algorithm
    # Time Complexity : O(E+V)
    # Space Complexity : O(E+V)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegrees = [0] * numCourses
        prerequisitesMapping = defaultdict(list)

        # Calculate the indegree for each vertex(course)
        for course,prerequisite in prerequisites:
            indegrees[prerequisite] += 1
            prerequisitesMapping[course].append(prerequisite)

        q = deque()

        # Collect all courses with indegrees as zero
        for c in range(numCourses):
            if indegrees[c] == 0:
                q.append(c)

        result = []
    
        while q:
            course = q.popleft()
            result.append(course) 
            # Reducing the indegrees of each neighbor 
            # and determining if the neighbor has no indegrees
            for prerequisite in prerequisitesMapping[course]:
                indegrees[prerequisite]-=1
                if indegrees[prerequisite] == 0:
                    q.append(prerequisite)

        # result variable hold the topological sort
        # If the no of vertices in result is less than the total vertices 
        # Then there is a cycle in the graph
        return True if len(result) == numCourses else False
            
        




        