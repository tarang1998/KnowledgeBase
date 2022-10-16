#https://leetcode.com/problems/string-compression-ii/description/

class Solution:


    

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @cache
        def dp(i,prev,prevCount,k):

            if(k<0):
                return float('inf')


            if(i == len(s)):
                return 0
            
        
            delete = dp(i+1,prev,prevCount,k-1)

            keep = None

            if(s[i] == prev):

                keep = dp(i+1,prev,prevCount+1,k)

                if prevCount in [1,9,99]:
                    keep += 1

            
            else:
                keep = dp(i+1,s[i],1,k) + 1
            
            return min(keep,delete)


        return dp(0,"",0,k)




            



            



        

        

