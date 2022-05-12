class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        que= deque(students)
        c,i=0,0
        while c!=len(que):
            if sandwiches[i]==que[0]:
                i+=1
                que.popleft()
                c=0
            else:
                que.append(que.popleft())
                c+=1
        return len(que)        
                