class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        
        l = len(arr)
        maxim = max(arr)
        clean = [[0,0] for i in range(maxim+1)]
        for number in set(arr):
            clean[number][1] = number
        print(len(arr))
        for number in arr:
            clean[number][0] += 1
        clean.sort(reverse = True)
        
        freq_sum = 0
        counter = 0
        for i in range(len(clean)):
            if(freq_sum >= l/2):
                break
            freq_sum += clean[i][0]
            counter += 1
        
        return counter