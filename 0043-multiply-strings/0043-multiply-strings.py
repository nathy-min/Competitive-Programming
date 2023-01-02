class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dic = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,'6' : 6, '7' : 7, '8' : 8, 
                '9' : 9}
        
        n1 = 0 
        n2 = 0
        
        for i in num1:
            n1 = n1 * 10 + dic[i]
            
        for i in num2:
            n2 = n2 * 10 + dic[i]
        
        result = str(n1 * n2)
        return (result)