class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sor=sorted(arr)
        k=[]
        c=0
        while arr!=sor:
            sliced=arr[:len(arr)-c]
            a=max(sliced)
            b=arr.index(a)
            temp=arr[:b+1]
            temp.reverse()
            arr[:b+1]=temp
            tem=arr[:len(arr)-c]
            tem.reverse()
            arr[:len(arr)-c]=tem
            k.append(b+1)
            k.append(len(arr)-c)
            c+=1
        return k    