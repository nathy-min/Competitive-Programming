class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        longest_sub = 0
        @cache
        def backtrack(left, right):
            if left > right:
                return 0
            if left == right:
                return 1

            var1 = var2 = 0
            if  s[left] == s[right]:
                var1 = 2 + backtrack(left + 1, right - 1)
            else:
                var2 = max(backtrack(left + 1, right), backtrack(left, right - 1))          

            return var1 + var2

           

        return backtrack(0, n - 1)