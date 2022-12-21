n, m = map(int, input().split())

# convetring the mapping to list
data = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness = 0
for i in range(len(data)):
    if data[i] in set_a:
        happiness += 1
    elif data[i] in set_b:
        happiness -= 1
print(happiness)            
        
