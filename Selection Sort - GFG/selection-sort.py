#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        min = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[min]):
                min = j
        return min

    def selectionSort(self, arr, n):
        # code here
        for j in range(n):
            min = self.select(arr, j)
            if min != j:
                temp = arr[min]
                arr[min] = arr[j]
                arr[j] = temp
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends