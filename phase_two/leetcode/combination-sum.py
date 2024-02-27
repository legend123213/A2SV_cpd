class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def recu(summ,ptr,num):
            if summ==target and tuple(num[:]) not in res:
                res.add(tuple(num[:]))
                return
            for i in range(ptr,len(candidates)):
                if summ+candidates[i] <= target:
                    summ+=candidates[i]
                    num.append(candidates[i])
                    recu(summ,i,num)
                    k = num.pop()
                    summ-=k
        recu(0,0,[])
        return res
        