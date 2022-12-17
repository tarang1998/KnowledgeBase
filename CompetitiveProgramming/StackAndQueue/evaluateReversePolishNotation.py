class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            '+' : lambda x,y: x+y,
            '-' : lambda x,y: x-y,
            '*' : lambda x,y: x*y,
            '/' : lambda x,y: int(x/y)
        }

        stack = []

        for i in range(0,len(tokens)):
            if(tokens[i] in operations):
                rightOperand = stack.pop()
                leftOperand = stack.pop()

                result = operations[tokens[i]](leftOperand,rightOperand)
                stack.append(result)

            else:
                stack.append(int(tokens[i]))

        

        return stack[0]

                




    def evalRPNListElementDeletion(self, tokens: List[str]) -> int:

        i = 2

        while(i < len(tokens)): 
           
            if(tokens[i] == '+'):
                operand1 = int(tokens[i-2])
                operand2 = int(tokens[i-1])

                value = operand1 + operand2
                tokens.insert(i-2,value)
                del tokens[i-1:i+2]
                i -= 2

            elif(tokens[i] == '-'):
                operand1 = int(tokens[i-2])
                operand2 = int(tokens[i-1])

                value = operand1 - operand2
                tokens.insert(i-2,value)
                del tokens[i-1:i+2]
                i -= 2
            
            elif(tokens[i] == '*'):
                operand1 = int(tokens[i-2])
                operand2 = int(tokens[i-1])

                value = operand1 * operand2
                tokens.insert(i-2,value)
                del tokens[i-1:i+2]
                i -= 2

            elif(tokens[i] == '/'):
                operand1 = int(tokens[i-2])
                operand2 = int(tokens[i-1])

                value = int(operand1 / operand2)
                tokens.insert(i-2,value)
                del tokens[i-1:i+2]
                i -= 2

            else:
                i+=1

        return int(tokens[0])

