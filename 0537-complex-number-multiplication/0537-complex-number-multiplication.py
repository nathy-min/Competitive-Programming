class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        
        real1 = int(num1[0])
        imag1 = int(num1[1][:-1])
        real2 = int(num2[0])
        imag2 = int(num2[1][:-1])
        
        real = real1 * real2 - imag1 * imag2
        imag = real1 * imag2 + real2 * imag1
        result = str(real) + "+" + str(imag) + "i"
        return result
        