class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair=[ [p,i] for p,i in zip(position,speed)]
        stack=[]
        for p,i in sorted(pair)[::-1]:
            stack.append((target-p)/float(i))
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
                 
        return len(stack)