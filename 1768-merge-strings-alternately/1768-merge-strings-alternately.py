class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_word = ""
        size1 = len(word1)
        size2 = len(word2)
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < size1 and ptr2 < size2:
            final_word += word1[ptr1] + word2[ptr2]
            ptr1 += 1
            ptr2 += 1
            
        if ptr1 < size1:
            final_word += word1[ptr1:size1]
            
        if ptr2 < size2:
            final_word += word2[ptr2:size2]
            
        return final_word    