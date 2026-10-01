class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        right_max = -1

        for i in reversed(range(len(arr))):
            res[i] = right_max
            right_max = max(right_max, arr[i])
        return res