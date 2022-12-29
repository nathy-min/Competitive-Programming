if __name__ == '__main__':
    N = int(input())
lis = []
for i in range(N):
    inputes = input().split()
    if inputes[0] == "insert":
        lis.insert(int(inputes[1]), int(inputes[2]))
    elif inputes[0] == "print":
        print(lis)
    elif inputes[0] == "append":
        lis.append(int(inputes[1]))
    elif inputes[0] == "remove":
        lis.remove(int(inputes[1]))
    elif inputes[0] == "sort":
        lis.sort() 
    elif inputes[0] == "pop":
        lis.pop()
    elif inputes[0] == "reverse":
        lis.reverse()
        
