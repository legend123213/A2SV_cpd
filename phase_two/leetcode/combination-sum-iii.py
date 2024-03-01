class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()
        def helper(ls,summ,ind):
            if summ>n or len(ls)>9:
                return 
            if summ == n and len(ls) == k:
                res.add(tuple(ls))
                return
            for i in range(ind,10):
                ls.append(i)
                summ+=i
                helper(ls,summ,i+1)
                summ-=ls.pop()
        helper([],0,1)
        return res

            

        