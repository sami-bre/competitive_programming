class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if(char == ")"):
                # bring out everything till (
                temp = []
                while(True):
                    out = stack.pop()
                    if(out == "("):
                        break
                    temp.append(out)
                    
                for item in temp:
                    stack.append(item)
                print(stack)
                # reverse the things
                # get them back in
            else:
                stack.append(char)
                
        return "".join(stack)
        