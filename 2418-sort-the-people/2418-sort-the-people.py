class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        size = len(names)
        for i in range(size ):
            temp_ptr = i
            for j in range(i , size):
                if heights[temp_ptr] < heights[j]:
                    temp_ptr = j
            heights[i], heights[temp_ptr] = heights[temp_ptr], heights[i]
            names[i], names[temp_ptr] = names[temp_ptr], names[i]
       
        return names           
                    
                    
                    