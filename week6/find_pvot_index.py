class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum = 0
        sum_array = []
        
        for num in nums:
            sum += num
            sum_array.append(sum)
            
        pvot = -1
        
        for i in range(len(sum_array)):
            if i==0:
                lsum = 0
            else:
                lsum = sum_array[i-1]
                
            if i==len(sum_array)-1:
                rsum = 0
            else:
                rsum = sum_array[-1] - sum_array[i]
                
            if lsum == rsum:
                pvot = i
                break
                
        return pvot
        