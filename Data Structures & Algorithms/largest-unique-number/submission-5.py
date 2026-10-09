class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        if 1 not in count.values():
            return -1
        else:
            return max([num for num in nums if count[num] == 1])