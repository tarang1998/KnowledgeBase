from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        Time Complexity: O(V + E) where V = numCourses, E = number of prerequisites
        Space Complexity: O(V + E) for the graph, in-degree list, and queue
        """

        # Step 1: Create a graph and in-degree array
        graph = defaultdict(list)         # key: course, value: list of courses that depend on it
        in_degree = [0] * numCourses      # in_degree[i] = number of prerequisites for course i

        # Step 2: Fill the graph and in-degree array using prerequisites
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # To take 'course', you must first take 'prereq'
            in_degree[course] += 1        # One more prerequisite needed for 'course'

        # Step 3: Add all courses that have NO prerequisites to the queue
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)           # These courses can be taken right away

        # Step 4: Build the course order
        course_order = []

        while queue:
            current = queue.popleft()     # Take this course now
            course_order.append(current)  # Add to the final order

            # Look at all courses that need the current course
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1  # One less prerequisite to wait for
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)  # If no prereqs left, add to queue

        # Step 5: If we finished all courses, return the order. Else, return empty list
        if len(course_order) == numCourses:
            return course_order
        else:
            return []  # There’s a cycle; not all courses can be finished
