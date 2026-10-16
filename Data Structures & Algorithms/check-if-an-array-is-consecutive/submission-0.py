class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        min_val = min(nums)
        nums.sort()
        for i, num in enumerate(nums):
            if i != (num - min_val):
                return False
        return True
