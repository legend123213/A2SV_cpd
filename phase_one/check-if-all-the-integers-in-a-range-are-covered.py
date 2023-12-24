class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [0]*51
        for i in ranges:
            l = i[0]
            r = i[1]+1 
            arr[l:r] = [1 for i in range(r-l)]
        test = sum(arr[left:right+1]) if left !=right else arr[left]
        if test == right - left +1:
            return True
        else:
            return False

        