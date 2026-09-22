class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            ans[i] = max_val
            max_val = max(arr[i], max_val)
        return ans