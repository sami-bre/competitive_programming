class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
    
        bp = 0  # backward pointer
        for fp in range(len(nums)):
            if nums[fp] != nums[bp]:
                bp += 1
                nums[bp] = nums[fp]
                
        return bp+1
        