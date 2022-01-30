class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        fp = 0  # forward pointer
        bp = len(numbers)-1 # backward pointer
        
        while fp != bp:
            sum = numbers[fp] + numbers[bp]
            if sum == target:
                return [fp+1, bp+1]
            elif sum < target:
                fp += 1
            elif sum > target:
                bp -= 1
            