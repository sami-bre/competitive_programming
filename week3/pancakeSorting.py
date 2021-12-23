class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        l = len(arr)
        answer = []
        for i in range(l):
            maxim = max(arr[:l-i])
            ind = arr.index(maxim)
            if(ind != 0):
                answer.append(ind+1)
                # print(arr)
                # print(i)
                arr[:ind+1] = arr[:ind+1][::-1]
            
            answer.append(l-i)
            arr[:l-i] = arr[:l-i][::-1]
        
        return answer
        