class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        counter = 0
        start = 0
        end = 0
        nums.sort()
        
        # find the end
        try:
            end = nums.index(k)
        except ValueError:
            for index in range(len(nums)):
                if(nums[index] > k):
                    end = index-1
                    break
                elif(index+1 == len(nums)):
                    end = len(nums)-1
        
        
        while(start < end):
            if(nums[end]+nums[start]<k):
                start += 1
            elif(nums[end]+nums[start]>k):
                end -= 1
            elif(nums[end]+nums[start] == k):
                start += 1
                end -= 1
                counter += 1
        
        return counter
        
                
        