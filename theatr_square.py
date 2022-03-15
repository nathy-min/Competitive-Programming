import math
inputs = input().split()
n = int(inputs[0])
m = int(inputs[1])
a = int(inputs[2])
print(math.ceil(n / a) * math.ceil(m / a))
