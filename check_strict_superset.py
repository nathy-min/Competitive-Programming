A = set(map(int, input().split()))
n = int(input())
result = True

for i in range(n):
    set_n = set(map(int, input().split()))
    len_setn = len(set_n)
    len_A = len(A)
    if not set_n.issubset(A) or len_setn >= len_A:
        result = False
        break
      
print(result)  
