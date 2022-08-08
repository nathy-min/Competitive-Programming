class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        c= Counter(words)
        
        c=[(-v,k) for k,v in c.items()]
        heapq.heapify(c)

        res=[]
        i=0
        while i<k and len(c)!=0:
            res.append(heapq.heappop(c)[1])
            print(c)
            i+=1
            
        return res    