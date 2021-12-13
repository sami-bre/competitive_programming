class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # first do an insertion sort
        for i in range(len(nums)):
            subject = nums[i]
            for j in reversed(range(i)):
                if(subject<nums[j]):
                    nums[j+1] = nums[j]
                    if(j == 0):     # the case of the first element
                        nums[0] = subject
                else:
                    nums[j+1] = subject
                    break
        
        indices = []
        for i in range(len(nums)):
            if(nums[i] == target):
                indices.append(i)

        return indices
                
        