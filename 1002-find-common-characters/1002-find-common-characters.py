class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr_words = {}
        size = len(words)
        common_letters = []
        
        for i in range(size):
            arr_words[i] = [0 for i in range(26)]
            for j in words[i]:
                curr_count = words[i].count(j)
                idx = (ord(j) - 97)
                if arr_words[i][idx]:
                    continue
                arr_words[i][idx] += curr_count

        for i in range(26):
            temp = [word[i] for word in arr_words.values()]
            
            arr_words[0][i] = min(temp)
            if arr_words[0][i] > 0:
                for j in range(arr_words[0][i]):
                    print(chr(i))
                    common_letters.append(chr(i + 97))
                    
                    
        return common_letters
        
                    
                
                
            
            
        