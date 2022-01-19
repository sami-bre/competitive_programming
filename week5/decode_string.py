class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if(s[i] == ']'):
                temp_list = []
                while(stack[-1]!="["):
                    temp_list.append(stack.pop(-1))
                stack.pop()
                
                # find the number before the opening brace .... 
                temp_number = []
                while(stack[-1] in "0123456789"):
                    temp_number.append(stack.pop(-1))
                    if(len(stack) == 0):
                        break
                r = int("".join(temp_number[::-1]))
                temp_number = []

                # use the number you found and build the decoded string
                for _ in range(int(r)):
                    for ind in reversed(range(len(temp_list))):
                        stack.append(temp_list[ind])
                temp_list = []
            else:
                stack.append(s[i])
                
        return "".join(stack)