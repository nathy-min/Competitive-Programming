T = int(input())
for i in range(T):
    n = int(input())    
    cube_len = list(map(int,input().split()))
    i,j = 0,n-1
    if cube_len[i] >= cube_len[j]:
        blocked=[cube_len[i]]
    else:
        blocked = [cube_len[j]] 
    result = 'Yes'      
    
    while j>= i:
        
        if cube_len[i]>= cube_len[j] and blocked[-1] >= cube_len[i]:
            blocked.append(cube_len[i])
            i += 1
        elif cube_len[j]> cube_len[i] and blocked[-1] >= cube_len[j]:
            blocked.append(cube_len[j])
            j -= 1
        else:
            result = 'No'
    print(result)
