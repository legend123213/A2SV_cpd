from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        co = Counter(candidates)
        can = list(set(candidates))
        def helper(ptr,le,su):
            if su == target:
                res.add(tuple(sorted(le[:])))
                return True
            if su > target or len(le)>=len(candidates):
                return
            
            for i in range(ptr,len(can)):
                if co[can[i]]!=0:
                    le.append(can[i])
                    su += can[i]
                    co[can[i]]-=1
                    helper(ptr,le,su)
                    temp = le.pop()
                    su-=temp
                    co[temp]+=1
                    

            
                
        helper(0,[],0)
        return res
        