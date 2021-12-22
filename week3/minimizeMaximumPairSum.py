class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        maxim = nums[0] + nums[-1]
        l = len(nums)
        for i in range(l):
            if(nums[i]+nums[l-i-1] > maxim):
                maxim = nums[i]+nums[l-i-1]
        
        return maxim