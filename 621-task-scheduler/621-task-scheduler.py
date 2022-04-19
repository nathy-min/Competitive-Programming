class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count=Counter(tasks)
        maxh=[-c for c in count.values()]
        heapq.heapify(maxh)
        time =0
        q=deque()
        while maxh or q:
            time += 1
            if maxh:
                c= 1+heapq.heappop(maxh)
                if c:
                    q.append ([c,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxh,q.popleft()[0])
        return time        