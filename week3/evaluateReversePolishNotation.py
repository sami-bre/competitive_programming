class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if(tokens[i] in ["+", "-", "*", "/"]):
                a = stack.pop()
                b = stack.pop()
                if(tokens[i] == "+"):
                    stack.append(int(b)+int(a))
                elif(tokens[i] == "-"):
                    stack.append(int(b)-int(a))
                elif(tokens[i] == "*"):
                    stack.append(int(b)*int(a))
                else:   # division
                    
                    stack.append(int(int(b)/int(a)))
                print(f"calculated: {stack[-1]}")
            else:
                stack.append(tokens[i])
                
        print(len(stack))
        return stack[-1]