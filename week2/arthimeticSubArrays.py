class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        answer = [True for i in range(len(l))]
        for i in range(len(l)):
            subArray = nums[l[i]:r[i]+1]
            subArray.sort()
            gap = subArray[1] - subArray[0]
            for j in range(len(subArray)-1):
                if(subArray[j+1] - subArray[j] != gap):
                    answer[i] = False
                    break
                    
        return answer