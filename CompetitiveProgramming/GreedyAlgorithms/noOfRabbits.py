class Solution:

    # Time Complexity : O(n)
    def numRabbits(self, answers: List[int]) -> int:

        result = 0 
        mem = defaultdict(int)

        # Calculating the number of rabbits who say there are x other people in the group
        # Eg : [1,1,2] : There are 2 rabbits that say thee is 1 rabbit in the group with the sane color
        for answer in answers:
            mem[answer] += 1 

        # key : Rabbit count
        # count : No of rabbits who say there are (key) no of other rabbits in the group 
        for key,count in mem.items():
           
            # Finding groups
            # Eg1 : [1,1,1,1,2,1]
            # With key as 1 , 2 groups can be formed 
            # [1,1](2 red rabbits),[1,1](2 blue rabbits) each with the same color

            # Eg2 : [2,2,2,4,2,2,5,2,2,2]
            # 2 groups : [2,2,2] (3 red rabbits), [2,2,2] (3 blue rabbits)
            d = count // (key + 1)
            result += d * (key + 1 ) 


            # In Eg1 with key=1, r = [1] (consider 2 green rabbits, as only 1 answer is present )
            # In Eg2 with key=2, r = [2,2] (consider 3 green rabbits, since we need to calculate min no, assume 1 answer is missing)
            # These can be considered as groups with a different color 
            r = count % (key + 1)            
            if r != 0:
                result += key + 1 


        return result






        