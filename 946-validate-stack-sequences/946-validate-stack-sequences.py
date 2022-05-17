class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        n=len(popped)
        i=0
        for p in pushed:
            stack.append(p)
            while  stack and i<n and stack [-1]== popped[i]:
                i+=1
                stack.pop()
        return stack ==[]        