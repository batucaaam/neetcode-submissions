class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        comp_color = image[sr][sc]
        if comp_color == color:
            return image
        ROWS, COLS = len(image), len(image[0])

        def helper(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or image[r][c] != comp_color):
                return

            image[r][c] = color

            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c + 1)
            helper(r, c - 1)
        helper(sr, sc)
        return image