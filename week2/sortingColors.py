class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # BUBBLE SORT
        # for i in range(1,len(nums)):
        #     for j in range(1,len(nums)):
        #         if(nums[j] < nums[j-1]):
        #             nums[j], nums[j-1] = nums[j-1], nums[j]
        
        # COUNTING SORT
        freq = [0,0,0]
        for i in nums:
            freq[i] += 1
    
        nums.clear()
        
        # counting sort is an 'n' complexity algorithm. there must be some way to potimize the code below
        for n, f in enumerate(freq):
            for i in range(f):
                print(f"appending{n}")
                nums.append(n)
                
        