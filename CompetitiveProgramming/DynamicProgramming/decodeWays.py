class Solution:

    def numDecodings(self, s: str) -> int:

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


        

