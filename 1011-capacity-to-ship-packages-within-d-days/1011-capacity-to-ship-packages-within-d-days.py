class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def logic(cap):
            d = 1
            l = cap
            for i in weights:
                if l - i >= 0:
                    l-=i
                else:
                    l = cap
                    d += 1
                    l-=i
            return d
        res = "DN"
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l+r)//2
            if logic(m) > days:
                l = m + 1
            else:
                r = m - 1
                res = m
        return res