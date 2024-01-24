class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res, n = [], len(arr)
        for i in range(n,0,-1):
            pl = arr.index(i)
            if pl == i-1: continue
            if pl != 0:
                res.append(pl+1)
                arr[:pl+1] = arr[:pl+1][::-1]
            res.append(i)
            arr[:i] = arr[:i][::-1]
            
        
        return res
        