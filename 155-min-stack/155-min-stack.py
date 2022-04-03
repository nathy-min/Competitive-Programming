class MinStack(object):

    def __init__(self):
        self.s=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.s.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.s)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()