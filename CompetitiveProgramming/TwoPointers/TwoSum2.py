class Solution:

    # Time Complexity : O(n)
    def twoSum(self,numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: one at the start, one at the end
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            # If we found the correct sum, return 1-based indices
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                # Move left pointer to increase the sum
                left += 1
            else:
                # Move right pointer to decrease the sum
                right -= 1

            