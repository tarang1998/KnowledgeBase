class Solution:

    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0 

        right = len(numbers) - 1

        while(left < right):

            t = numbers[left] + numbers[right] 

            if(t < target):
                left += 1
                continue 

            elif(t == target):
                return [left + 1, right + 1]

            else:
                right-=1

       