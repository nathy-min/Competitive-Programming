if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

tuple_list = tuple(integer_list)

        

result = hash(tuple_list)  
print(result)      
    
