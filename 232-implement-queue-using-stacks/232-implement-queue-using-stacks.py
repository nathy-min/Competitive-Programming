class MyQueue(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)    
        

    def pop(self):
        """
        :rtype: int
        """
        if self.s2:
            return self.s2.pop()
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()   
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.s2:
            return self.s1[0]
        else:
            return self.s2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.s1 and not self.s2:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()