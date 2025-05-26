class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i = len(num1)-1
        j = len(num2)-1
        
        carry = 0 
        result= []

        while i>=0 or j>=0:

            d1 = ord(num1[i])-ord('0') if i>=0 else 0
            d2 = ord(num2[j])-ord('0') if j>=0 else 0

            dsum = d1+d2+carry
            result.append(dsum%10)
            carry = dsum//10


            i-=1
            j-=1


        if carry != 0:
            result.append(carry)

        return "".join(str(x) for x in result[::-1])



        