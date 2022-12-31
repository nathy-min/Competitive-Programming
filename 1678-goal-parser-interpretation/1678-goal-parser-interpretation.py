class Solution:
    def interpret(self, command: str) -> str:
        ptr = 0
        result = ""
        size  = len(command)
        
        while ptr < size:
            if command[ptr] == "G":
                result += "G"
                ptr += 1
            else:
                if command[ptr + 1] == ")":
                    result += "o"
                    ptr += 2
                else:
                    result += "al"
                    ptr += 4
                
        return result        