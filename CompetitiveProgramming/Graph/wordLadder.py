from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Time Complexity: O(N * M^2), where:
            N = number of words in wordList
            M = length of each word
        Space Complexity: O(N * M) for the pattern dictionary and visited set
        """

        # If endWord is not even in the dictionary, we can't reach it
        if endWord not in wordList:
            return 0

        # Add beginWord to the word list for processing patterns
        wordList.append(beginWord)

        # Step 1: Build a pattern map
        # For example, 'hot' -> '*ot', 'h*t', 'ho*'
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)

        # Step 2: Initialize BFS
        q = deque()
        q.append(beginWord)
        visited = {beginWord: 1}  # Track words we’ve already used
        steps = 1  # Start with 1 since beginWord counts as step 1

        # Step 3: Use BFS to find the fastest way from start to goal 
        while q:
            for _ in range(len(q)):
                word = q.popleft()

                # If we’ve reached the endWord, return the step count
                if word == endWord:
                    return steps

                # Generate all patterns for the current word
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]

                    # Check all words that match the current pattern
                    for neighbor in patterns[pattern]:
                        if neighbor not in visited:
                            visited[neighbor] = 1
                            q.append(neighbor)

            # After one full level of BFS, increment step count
            steps += 1

        # If we finish BFS without finding endWord, return 0
        return 0
