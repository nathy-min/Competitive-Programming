def heapify(self,arr, n, i):
        large = i
        left = 2*i+1
        right = 2*i+2
        
        if (left < n and arr[left] > arr[large]):
            large = left
        if (right < n and arr[right] > arr[large]):
            large = right
        if large != i:
            arr[i], arr[large] = arr[large], arr[i]
            self.heapify(arr, n, large)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        i = n-2
        while i>=0:
            self.heapify(arr, n, i)
            i -= 1
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        i = n-1
        while i>=0:
            arr[0],arr[i] = arr[i],arr[0]
            self.heapify(arr,i,0)
            i -= 1
