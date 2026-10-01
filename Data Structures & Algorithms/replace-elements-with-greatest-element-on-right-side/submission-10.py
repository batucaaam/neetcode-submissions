class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        max_val = -1

        for i in reversed(range(len(arr))):
            res[i] = max_val
            max_val = max(arr[i], max_val)
        return res