class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        answer=1994
        
        
        """
        values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        answer=values[s[0]]
        for i in range(1,len(s)):
            if values[s[i]]>values[s[i-1]]:
                answer-=2*values[s[i-1]]
            answer+=values[s[i]]
        return answer            