class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_idx = arr.index(max(arr))
        ans = True
        left_ptr = 0
        right_ptr = len(arr) - 1
        
        if len(arr) < 3 or max_idx == left_ptr or max_idx == right_ptr:
            return False
        
        while left_ptr < max_idx:
            if arr[left_ptr] >= arr[left_ptr + 1]:
                ans = False
            left_ptr += 1
            
        while right_ptr > max_idx:
            if arr[right_ptr] >= arr[right_ptr - 1]:
                ans = False
            right_ptr -= 1
            
        return ans    
                
            