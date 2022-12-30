class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        S = list(s)
        T = list(t)
        for char in T:
            if char in S:
                S.remove(char)
                continue
            else:
                return char
        