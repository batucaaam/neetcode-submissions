class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in valMap:
                return [valMap[diff], i]
            valMap[nums[i]] = i
                