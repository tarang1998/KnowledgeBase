from collections import defaultdict, deque

class Solution:

    # Time Complexity: O(V+E)
    # Space Complexity : O(V+E)
    def canFinish(numCourses, prerequisites):
        # Build a graph of all the courses and their prerequisites
        graph = defaultdict(list)  # This will store which courses depend on each course
        in_degree = [0] * numCourses  # This keeps track of how many prereqs each course has

        # Go through each prereq pair and fill out the graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # Add an arrow from prereq -> course
            in_degree[course] += 1        # course has one more thing it needs before it can be taken

        # Start with courses that don't need any prerequisites
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:  # This course can be taken right away
                queue.append(i)

        # Count how many courses we were able to "finish"
        finished_courses = 0

        while queue:
            current = queue.popleft()  # Take a course that can be done now
            finished_courses += 1      # Yay, one more course done!

            # Go through every course that depends on the current course
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1  # One less prereq to wait for
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)  # Now we can take this course too!

        # If we finished all the courses, return True
        return finished_courses == numCourses
