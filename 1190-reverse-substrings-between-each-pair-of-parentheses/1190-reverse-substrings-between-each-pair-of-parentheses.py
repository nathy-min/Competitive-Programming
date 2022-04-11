class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i in '()':
                if i == ')':
                    word = stack.pop()
                    if(word != '('):
                        stack.pop()
                        last = len(stack) - 1
                        if(last >= 0 and stack[last] not in  '()'):
                            stack[last] += word[::-1]
                        else:
                            stack.append(word[::-1])
                else:
                    stack.append(i)
            else:
                last = len(stack) - 1
                if(last >= 0):
                    if stack[last] in '()':
                        stack.append(i)
                    else:
                        stack[last] += i
                else:
                    stack.append(i)
        return stack[0]
        