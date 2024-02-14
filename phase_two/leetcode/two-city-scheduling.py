class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        k = sorted(costs,key = lambda x : x[0]-x[1])
        res = 0
        mid = len(k)//2
        for i in range(mid):
            res+=k[i][0]+k[i+mid][1]
        return res
        