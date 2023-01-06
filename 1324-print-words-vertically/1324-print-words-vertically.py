class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()
        
        word_max_length = 0
        for word in words:
            word_max_length = max(len(word), word_max_length)
        output = [[" " for word in words] for index in range(word_max_length)]
        
        for index in range(len(words)):
            for idx in range(len(words[index])):
                output[idx][index] = words[index][idx]
              
        for idx in range(len(output)):
            while output[idx][-1] == " ":
                output[idx].pop()
        
        for idx in range(len(output)):
            output[idx] = "".join(output[idx])
            
        return output  
        