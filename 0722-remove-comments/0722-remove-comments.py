class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        string = '#'.join(source)
        answer_str = ''
        answer = []
        indx = 0
        size = len(string)

        while indx < size :
            if string[indx] == '/':
                ptr = indx + 2
                if indx + 1 < size and string[indx + 1] == "*":
                    while string[ptr:ptr+2] != '*/' :
                        ptr += 1
                    indx = ptr + 2

                elif indx + 1 < size and string[indx + 1] == "/":
                    while ptr < size and string[ptr] != "#"  :
                        ptr += 1
                    indx = ptr
                else:
                    answer_str += string[indx]
                    indx += 1


            else:
                answer_str += string[indx]
                indx += 1 
        answer = answer_str.split('#')
        ans = []
        for i in answer:
            if i:
                ans.append(i)
        
        return ans                           
                    
                    

