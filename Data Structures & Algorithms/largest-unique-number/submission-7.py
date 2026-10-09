class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        return max([num for num in nums if count[num] == 1], default = -1)