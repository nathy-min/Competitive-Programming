class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = list(string.ascii_lowercase)
        mapped_value = [str(i) for i in range(1,10)]
        rest_value = [str(i) + "#" for i in range(10,27)]
        mapped_value += (rest_value)
        mapped_str = ''
        dic = {}
        size = len(s)
        
        for i in range(26):
            dic[mapped_value[i]] = alphabet[i]
        
        ptr = 0
        while ptr < size:
            if ptr + 2 < size and s[ptr+2] == "#":
                mapped_str += dic[s[ptr:ptr+3]]
                ptr += 3
                
            else:
                mapped_str += dic[s[ptr]]
                ptr += 1
            
        return mapped_str    
        