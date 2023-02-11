class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        total_sum = sum(skill)              # Total sum
        n = len(skill)
        
        total_no = n//2              # No of pairs
                
        desired = total_sum // total_no        # Desired sum of each pair
                
        skill.sort()
        
        chemistry_tot = 0
        
        l = 0                           # Two Pointer (Two Sum)             
        r = n-1
        
        while l<r:
            if skill[l]+skill[r]==desired:
                chemistry_tot+=skill[l]*skill[r]
            else:
                return -1
            l+=1
            r-=1
            
        return chemistry_tot
        