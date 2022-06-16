class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        c=0
        l,r=0,len(people)-1
        while r>= l:
            if people[l]+ people[r]> limit:
                r -=1
                c+=1
            else:
                c+=1
                r-=1
                l+=1
        return c        