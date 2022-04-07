#https://leetcode.com/problems/next-permutation/
#https://www.tutorialspoint.com/next-permutation-in-python

# The lexicographically next permutation is basically the greater permutation. 
# For example, the next of “ACB” will be “BAC”. 
# In some cases, the lexicographically next permutation is not present, like “BBB” or “DCBA” etc.

# 1 2 3 4 5 -> 1 2 3 5 4 

# 1 3 5 4 2 -> 1 4 2 3 5

# We need to find the first pair of two successive numbers a[i] and a[i−1], from the right, 
# which satisfy a[i]>a[i−1]. (In the case of [1 3 5 4 2] => (3,5))

# Now, no rearrangements to the right of a[i−1] can create a larger permutation 
# since that subarray consists of numbers in descending order. 
# (No arrangement to the right of 3 could create a larger permutation, as they are already arranged in descending order : [5 4 2])

# Thus, we need to rearrange the numbers to the right of a[i−1] including itself.
# Now, what kind of rearrangement will produce the next larger number? 
# We want to create the permutation just larger than the current one. 
# Therefore, we need to replace the number a[i−1] with the number which is just larger 
# than itself among the numbers lying to its right section, say a[j]
# (Will need to replace 3 with 4 , the number which is just larger than it )

# We swap the numbers a[i−1] and a[j]. 
# We now have the correct number at index i−1. 
# But still the current permutation isn't the permutation that we are looking for. 
# We need the smallest permutation that can be formed by using the numbers only to the right of a[i−1]. 
# Therefore, we need to place those numbers in ascending order to get their smallest permutation.
# (After swapping : [1 4 5 3 2] : The no right of 4 need to be sorted in ascending order to get the next permutation)

# But, recall that while scanning the numbers from the right, we simply kept decrementing the index until we found the pair 
# a[i] and a[i−1] where, a[i] > a[i-1]. 
# Thus, all numbers to the right of a[i−1] were already sorted in descending order. **
# Furthermore, swapping a[i−1] and a[j] didn't change that order. 
# Therefore, we simply need to reverse the numbers following a[i−1] to get the next smallest lexicographic permutation.
# (In [1 3 5 4 2 ] : The no after 3 are in descending order and after swapping : [1 4 5 3 2] : The no's after 4 are still in descending order)
# (We need to reverse the numbers after 4)

# Eg with repeating Nos

# (1 3 3 2 1 -- swap --> 2 3 3 1 1 -- reverse --> 2 1 1 3 3)
# (2 1 1 3 3 -- swap --> 2 1 3 3 1 -- reverse --> 2 1 3 1 3)

# (2 3 1 3 3 -- swap --> 2 3 3 3 1 -- reverse --> 2 3 3 1 3)

#Time Complexity : O(n)
#Space Complexity : O(1)

class Solution:
    def nextPermutation(self,nums):

        decreasingSequenceOfNumberFromTheRightFound = False

        i = len(nums)-2

        while (i>=0):

            if(nums[i] < nums[i+1]):
                
                decreasingSequenceOfNumberFromTheRightFound = True
                break

            i-=1

        # If decreasing Sequence not found
        # The array is already sorted in the descending order 
        # We need to reverse it or sort it in ascending order
        if not decreasingSequenceOfNumberFromTheRightFound:
            nums.sort()

        else:
            maxIndex = self.findMaxIndex(nums,nums[i],i+1)
            nums[i],nums[maxIndex] = nums[maxIndex],nums[i]
            # reverse the list starting from i+1
            nums[i+1:] = nums[i+1:][:: -1]
        return nums
    

    def findMaxIndex(self,array, currentValue, fromIndex):

        maxValue = float('inf')
        maxIndex = -1

        # Could also find the max index by looping from the end of the array
        # As the array is arranged in the descending order
        # That Solution would be more optimum
        for i in range(fromIndex, len(array)):

            if(array[i] > currentValue and array[i] <= maxValue):
                maxValue = array[i]
                maxIndex = i

        return maxIndex
            
            




                


