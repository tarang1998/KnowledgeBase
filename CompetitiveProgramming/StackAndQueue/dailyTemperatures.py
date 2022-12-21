




        

class Solution:

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:

        result = [0]


        for i in range(len(temperatures)-2,-1,-1):

            current_temp = temperatures[i]

            next_greatest_temp = float('inf')

            for j in range(i+1, len(temperatures)):

                if (temperatures[j] > current_temp):

                    next_greatest_temp = temperatures[j]

                    break

            if(next_greatest_temp == float('inf')):
                result.insert(0,0)
            else:
                result.insert(0,j-i)

        return result

            
            









    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [len(temperatures)-1]

        ans = [0]

        for i in range(len(temperatures)-2,-1,-1):


            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if(len(stack)==0):
                ans.insert(0,0)
            else:
                ans.insert(0,stack[-1]-i)

            stack.append(i)

        return ans


        



