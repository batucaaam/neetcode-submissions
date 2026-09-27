class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = max_val = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
                max_val = max(curr, max_val)
            else:
                curr = 0
        return max_val