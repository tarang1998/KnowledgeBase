class Solution:

    mem = None


    def parse(self,s,wordDict):

        if s in self.mem:
            return self.mem[s]

        if(s == ""):
            return True 

        for word in wordDict:

            if(s.startswith(word)):
                
                us = s[len(word):]

                if(self.parse(us,wordDict)):
                    self.mem[s] = True 
                    return True

        #If no word matches the remaining string can't be resolved 
        #Caching the result for further computation
        self.mem[s] = False
        return False 

    #Creating a decision Tree At each point
    #Along with caching 
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:

        self.mem = {}

        return self.parse(s,wordDict)


    #BottomUp Approach
    #TimeComplexity : O(n*m*n)
    #Looping through each letter of the string -> n letters
    #For each letter checking the word list -> m words
    #Comparing the string with the word -> n letters , Assuming the word in the word list could be 
    #equal to the length of the string
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):

            for word in wordDict:

                if((i + len(word) <= len(s)) and s[i:i+len(word)] == word):
                    dp[i] = dp[i + len(word)]

                if(dp[i]):
                    break

        return dp[0]




