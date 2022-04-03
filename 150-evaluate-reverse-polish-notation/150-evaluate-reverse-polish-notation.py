class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opStack = []
        for token in tokens:
            if re.match("[-+]?\d+$", token):
                opStack.append(token)
            else:
                operand2 = int(opStack.pop())
                operand1 = int(opStack.pop())
                if token == "*":
                    opStack.append(operand1 * operand2)
                elif token == "/":
                    opStack.append(int(operand1 / operand2))
                elif token == "-":
                    opStack.append(operand1 - operand2)
                elif token == "+":
                    opStack.append(operand1 + operand2)
        return opStack.pop()
        