
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        u = []
        for key, value in count.items():
            u.append([key, value])
        u.sort(key = lambda a:a[1])
        result = []
        n = len(u)-1
        for i in range(k):
            result.append(u[n-i][0])
        return result
            