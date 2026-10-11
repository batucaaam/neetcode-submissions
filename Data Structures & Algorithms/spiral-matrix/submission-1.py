class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix and matrix[0]:  
            # Top
            res.extend(matrix.pop(0))
            # Right
            if matrix:
                for row in matrix:
                    res.append(row.pop())
            # Bottom
            if any(matrix):
                res.extend(matrix.pop()[::-1])
            # Left
            if any(matrix):
                for row in reversed(matrix):
                    res.append(row.pop(0))
        return res