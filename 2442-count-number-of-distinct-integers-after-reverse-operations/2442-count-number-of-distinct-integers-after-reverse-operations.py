class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        dct=defaultdict(int)
        for num in nums:
            dct[num]=1
        for num in nums:
            rev=int(str(num)[::-1])
            if dct[rev]!=1:
                dct[rev]=1
        return len(dct)