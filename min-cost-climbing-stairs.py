class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i <= 1:
                return cost[i]
            if i not in memo:
                memo[i] = min(dp(i - 1), dp(i - 2)) + cost[i]

            return memo[i]

        memo = {}
        cost.append(0)
        return dp(len(cost) - 1)