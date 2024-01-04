class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxi = max(arr)
        ptr = 0
        if len(arr)<=2:
            return False
        
        for i in range(1,len(arr)):
            if arr[i]<=arr[i-1]:
                ptr=i
                break
        if ptr == 1 or ptr-1 ==len(arr)-1:
            return False
        for j in range(ptr,len(arr)):
            if arr[j]>=arr[j-1]:
                return False
            
        return True
            

          