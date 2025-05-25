class Solution:
    def reverse(self, x: int) -> int:

        result = 0 
        
        isNegative = -1 if x < 0 else 1

        x = abs(x)

        while x:

            r = x % 10 

            x = x // 10

            print(x)

            result = result * 10 + r 

            if result > pow(2,31) - 1:
                return 0

        return result * isNegative



        