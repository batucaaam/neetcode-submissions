class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = []
        word2 = []
        for i in s:
            word1.append(i)
        for i in t:
            word2.append(i)
        return sorted(word1) == sorted(word2)
        