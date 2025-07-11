from collections import Counter, defaultdict

class Solution:
    # Time Complexity : O(n+m)
    # Space Complexity : O(n+m)
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary to count required characters from t
        t_count = Counter(t)
        required = len(t_count)  # Number of unique characters in t that must be in the window

        # Pointers for the window
        left = 0
        right = 0

        # formed: how many unique characters in current window match required frequency
        formed = 0
        window_counts = defaultdict(int)

        # (window_length, left_index, right_index)
        ans = (float("inf"), None, None)

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            # Check if current char completes the requirement from t
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            # Try to shrink the window while it's still valid
            while left <= right and formed == required:
                # Update answer if this window is smaller
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)

                # Pop from left
                char = s[left]
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1

                left += 1

            # Expand right pointer
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

   