class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arr[i] = max(arr[i + 1:], default = 0)
        arr[len(arr) - 1] = -1
        return arr