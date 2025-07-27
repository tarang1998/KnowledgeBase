from collections import defaultdict, deque
from typing import List

class Solution:
    # Time Complexity: O(N * L^2), where N = number of words, L = word length
    # Space Complexity: O(N * L)
  
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # If the endWord is not in the word list, there's no way to reach it
        if endWord not in wordList:
            return []

        wordList.append(beginWord)  # Ensure beginWord is also in wordList

        # Step 1: Build a pattern map
        # Each pattern like h*t maps to all words that match it like "hot", "hat"
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)

        # Step 2: Breadth-First Search (BFS) to build graph
        q = deque([beginWord])           # Queue for BFS
        visited = set([beginWord])       # Set to avoid revisiting
        parents = defaultdict(list)      # Store all parents that lead to a word

        found = False                    # Flag to stop when endWord is reached

        while q and not found:
            local_visited = set()        # Words visited at current level
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neigh in patterns[pattern]:
                        if neigh not in visited:
                            if neigh not in local_visited:
                                local_visited.add(neigh)
                                q.append(neigh)
                            # Add this word as a parent for backtracking later
                            parents[neigh].append(word)
                            if neigh == endWord:
                                found = True
            visited.update(local_visited)  # Mark this level's words as visited

        # If we never found the endWord
        if not found:
            return []

        # Step 3: Backtrack from endWord to beginWord using parent links
        res = []

        def backtrack(word, path):
            # Base case: we reached the beginWord
            if word == beginWord:
                res.append([beginWord] + path[::-1])
                return
            # Recursively backtrack all parents
            for parent in parents[word]:
                backtrack(parent, path + [word])

        backtrack(endWord, [])  # Start backtracking from the end
        return res
