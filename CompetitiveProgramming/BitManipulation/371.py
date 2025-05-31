class Solution:

    def getSum1(self, a: int, b: int) -> int:

        # Sum the binary numbers 
        # Each binary should have equal no of bits
        def sumbins(abin,bbin):
            carry = 0 
            binsum = []
            for i in range(len(abin)):
                r = (abin[i] + bbin[i] + carry )%2
                carry = (abin[i] + bbin[i] + carry)//2
                binsum.append(r)
            return binsum


        def convertToReverseBinary(num):
            isNegative = True if num<0 else False 
            binary = []
            num = abs(num)
            while num:
                binary.append(num%2)
                num = num//2
            n = len(binary)

            for i in range(0,12):
                if i > n-1:
                    binary.append(0) 
                # Representing negative no in 2s compliment 
                if isNegative:
                    if binary[i] == 0:
                        binary[i] = 1 
                    else:
                        binary[i] = 0
            if isNegative:
                binary = sumbins(binary, [1,0,0,0,0,0,0,0,0,0,0,0])
            return binary 



        abin = convertToReverseBinary(a)
        bbin = convertToReverseBinary(b)

        binary = sumbins(abin,bbin)[0:12]

        isResultNegative = False

        if binary[-1] == 1:
            isResultNegative = True
            for i in range(len(binary)):
                binary[i] = 1 if binary[i] == 0 else 0
            binary = sumbins(binary, [1,0,0,0,0,0,0,0,0,0,0,0])

        result = 0 

        for i in range(len(binary)):
            result += binary[i] * pow(2,i)

        return -result if isResultNegative else result



        
        
        




        