from collections import deque
class Solution:
    
    def isValid(self, s: str) -> bool:
        matches = {"(":")","{":"}","[":"]"}
        stack = deque()
        for i in range(len(s)):
            item = s[i]
            if(item in ['(','[','{']):
                stack.append(item)
            else:
                try:
                    if(item==matches[stack.pop()]):
                        pass
                    else:
                        return False
                except IndexError:
                    return False
        
        if(len(stack) == 0):
            return True
        else:
            return False
        
        
                
                
        
        