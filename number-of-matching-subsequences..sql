def sub(st):
            pos = -1
            for char in st:
                pos = s.find(char, pos+1)
                if pos == -1: return False
            return True
        return sum(map(sub, words))
	```
IF THIS HELP U KINDLY UPVOTE THIS TO HELP OTHERS TO GET THIS SOLUTION
IF U DONT GET IT KINDLY COMMENT AND FEEL FREE TO ASK
AND CORRECT MEIF I AM WRONG