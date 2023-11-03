class Solution:

    # Time Complexity : O(n^2)
    # Space Complexity : O(n) , depends on the sorting algorithm that is used 

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        # Sort the given array in the ascending order
        nums = sorted(nums)

        for i,num in enumerate(nums):

            # Skipping over if element is equal to the previous element 
            # All possible combinations with that starting element already found 
            if((i>0 and num == nums[i-1])):
                continue 

            # Finding the other two digits  
            # Very similar to the 2sum problem
            
            l = i+1
            r = len(nums)-1

            while(l<r):

                target = num + nums[l] + nums[r]

                # If target is greater than zero shift the right pointer 
                if (target > 0):
                    r -= 1

                # If the target is less than zero shift the left pointer
                elif (target < 0):
                    l += 1

                # If target is equal to zero 
                else:
    
                    res.append([num,nums[l], nums[r]])

                    l += 1

                    # Making sure duplicate triplets are not formed 
                    # if element is same , the possible combination has already been tried 
                    while(nums[l] == nums[l-1] and l < r):
                        l += 1

        return res


        



                









            



        