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
