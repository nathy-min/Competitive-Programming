class Solution:
    def candy(self, ratings: List[int]) -> int:
        n , stack = len(ratings) , [1]*len(ratings)
        
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                stack[i+1] = stack[i] + 1
                
        for i in range(n-2 , -1 , -1):
            if ratings[i] > ratings[i+1]:
                stack[i] = max(stack[i] , stack[i+1] + 1)
                
        return sum(stack)