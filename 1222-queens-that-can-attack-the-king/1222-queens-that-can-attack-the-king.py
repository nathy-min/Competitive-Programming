class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king:List[int]) -> List[List[int]]:
        ans = []
        for i in range(king[0] - 1, -1, -1):
            if [i, king[1]] in queens:
                ans.append([i, king[1]])
                break
        c1, c2 = king[0] - 1, king[1] - 1
        while c1 >= 0 and c2 >= 0:
            if [c1, c2] in queens:
                ans.append([c1, c2])
                break
            c1 -= 1
            c2 -= 1
        for i in range(king[1] - 1, -1, -1):
            if [king[0], i] in queens:
                ans.append([king[0], i])
                break
        for i in range(king[1] + 1, 8):
            if [king[0], i] in queens:
                ans.append([king[0], i])
                break
        c1, c2 = king[0] - 1, king[1] + 1
        while -1 < c1 and 8 > c2:
            if [c1, c2] in queens:
                ans.append([c1, c2])
                break
            c1, c2 = c1 - 1, c2 + 1
        c1, c2 = king[0] + 1, king[1] - 1
        while 8 > c1 and -1 < c2:
            if [c1, c2] in queens:
                ans.append([c1, c2])
                break
            c1 += 1
            c2 -= 1
        for i in range(king[0], 8):
            if [i, king[1]] in queens:
                ans.append([i, king[1]])
                break
        c1, c2 = king[0] + 1, king[1] + 1
        while 8 > c1 and 8 > c2:
            if [c1, c2] in queens:
                ans.append([c1, c2])
                break
            c1, c2 = c1 + 1, c2 + 1
        return ans