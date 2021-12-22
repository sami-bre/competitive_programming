class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        time_left = []
        data = sorted([(position[i], speed[i]) for i in range(len(position))])
        
        for i in range(len(position)):
            time_left.append((target-data[i][0])/data[i][1])
            
        stack = []
        
        for item in time_left:
            while(len(stack) != 0 and item >= stack[-1]):
                stack.pop()
            stack.append(item)
            
        return len(stack)