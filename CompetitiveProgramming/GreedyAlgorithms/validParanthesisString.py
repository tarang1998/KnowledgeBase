class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Greedy approach to validate parentheses with '*'.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        min_open = 0  # minimum possible open '(' count
        max_open = 0  # maximum possible open '(' count

        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # char == '*'
                min_open -= 1   # treat '*' as ')'
                max_open += 1   # treat '*' as '('

            # min_open can't be negative
            if min_open < 0:
                min_open = 0

            # If max_open is negative, too many ')'
            if max_open < 0:
                return False

        # All opens should be closed in the minimum case
        return min_open == 0

