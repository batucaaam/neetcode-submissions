class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for charS in s:
            if charS not in map:
                map[charS] = 1
            else:
                map[charS] += 1
        for charT in t:
            if charT not in map:
                return False
            elif map[charT] == 0:
                return False
            else:
                map[charT] -= 1
        return True
            

