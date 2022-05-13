class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        di=Counter(s)
        items=sorted(di.items(), key=lambda x: x[1], reverse=True)
        answer=''
        for i in items:
            answer+=i[0]*i[1]
        
        return answer