class Solution:

    # Time Complexity : O(n)
    # Space Compexity : O(n)
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:


        len1 = len(nums1)
        len2 = len(nums2)
        
        index1 = 0
        index2 = 0 

        idCounter = 1

        result = []

        while index1<len1 or index2<len2:

            valSum = 0 

            id1,val1 = nums1[index1] if index1<len1 else [-1,-1]
            id2,val2 = nums2[index2] if index2<len2 else [-1,-1]

            if id1 != idCounter and id2 != idCounter:
                idCounter += 1
                continue 

            if id1 == idCounter:
                valSum += val1
                index1 += 1 

            if id2 == idCounter:
                valSum += val2
                index2 += 1

            result.append([idCounter,valSum])
            idCounter += 1 

        return result
      



            
            





        