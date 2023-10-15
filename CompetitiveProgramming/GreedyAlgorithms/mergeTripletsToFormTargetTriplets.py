class Solution:

    # Time Complexity : O(n)
    
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a = target[0]
        b = target[1]
        c = target[2]

        a_p = False
        b_p = False
        c_p = False

        for triplet in triplets:

            # Check for the first element 
            if (triplet[0] == a and triplet[1]<= b and triplet[2] <= c):
                a_p = True

            # Check for the middle element
            if (triplet[1] == b and triplet[0] <= a and triplet[2] <= c):
                b_p = True

            # Check for the last element 
            if (triplet[2] == c and triplet[0] <= a and triplet[1] <= b):
                c_p = True 

            if(a_p and b_p and c_p):
                return True 

        
        return False

        