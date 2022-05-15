class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(temperatures)
        di={i:v for i,v in enumerate(temperatures)}
        stack=[]
        for i in range(len(di)):
            while stack and di[i] > stack[-1][1]:
                val=stack.pop()[0]
                answer[val]=i-val
            stack.append([i,di[i]])    
        return answer    