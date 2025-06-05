class Solution:


    def numDecodings(self, s: str) -> int:

        n = len(s)

        if n == 1:
            return 0 if s[0] == "0" else 1 

        dp = [0]*(n+1)
        dp[n] = 1 
        dp[n-1] = 0 if s[-1] == "0" else 1

        for i in range(n-2,-1,-1):
            d = int(s[i:i+2])
            if  d <= 26 and d>9 :
                dp[i] = dp[i+1] + dp[i+2]
            else:
                if s[i] == "0":
                    dp[i] = 0 
                    continue
                dp[i] = dp[i+1]
        return dp[0]

    def numDecodings1(self, s: str) -> int:

        mem = {}

        def parse(s,i):

            if(i in mem):
                return mem[i]

            if(s[i] == '0'):
                mem[i] = 0
                return 0 

            result = parse(s,i+1)

            if( i+1 < len(s) and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <=26):

                result += parse(s,i+2)

            mem[i] = result
            return result

        mem[len(s)] = 1

        parse(s,0)

        return mem[0]


        

