class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float('inf')
        second = float('inf')

        for ele in nums: 


            if(second < ele):
                return True
            if(ele <= first):
                first = ele
            else:
                second = ele
        
        return False





            


