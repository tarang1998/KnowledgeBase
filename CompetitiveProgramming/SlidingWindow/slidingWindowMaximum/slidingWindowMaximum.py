class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # To store indexes of the element in the sliding window
        dq = deque()

        # To store the maximum element in each sliding window
        maxes = []


        for i in range(len(nums)):

            # If the deque is not empty
            # And check if the index at the front is out of the sliding window
            # If true pop the element from the front of the queue 
            if dq and i-k >= dq[0]:

                dq.popleft()

            # While the queue is not empty
            # If the last elements value in the queue which is in the sliding window
            # Is less that the current Value pop the value
            while dq and nums[dq[-1]] <= nums[i]:

                dq.pop()


            dq.append(i)

            if(i >= k-1):
                maxes.append(nums[dq[0]])


        return maxes





    def maxSlidingWindowUsingBruteForce(self, nums: List[int], k: int) -> List[int]:


        n = len(nums)

        slidingWindowStartPointer = 0

        currentPointer = k-1

        output = []


        while(currentPointer <= n-1):


            output.append(max(nums[slidingWindowStartPointer:currentPointer+1]))

            slidingWindowStartPointer += 1

            currentPointer += 1

            

        return output