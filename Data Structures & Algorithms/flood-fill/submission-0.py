class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        comp_color = image[sr][sc]
        def helper(image, sr, sc, color):
            ROWS, COLS = len(image), len(image[0])
            if (min(sr, sc) < 0 or sr == ROWS or sc == COLS or image[sr][sc] == color):
                return 0
            if image[sr][sc] == comp_color:
                image[sr][sc] = color

                helper(image, sr + 1, sc, color)
                helper(image, sr - 1, sc, color)
                helper(image, sr, sc + 1, color)
                helper(image, sr, sc - 1, color)
        helper(image, sr, sc, color)
        return image