class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        data = [0 for i in range(len(temperatures))]
        monstack = []
        # temperatures.reverse()
        length = len(temperatures)
        for index in range(length-1,-1,-1):
            while(len(monstack) != 0 and temperatures[index] >= temperatures[monstack[-1]]):
                monstack.pop()
                
            if(len(monstack) != 0):
                data[index] = monstack[-1] - index
                
            monstack.append(index)      
                
        return data