from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        co = Counter(nums)
        l = sorted(co,reverse=True)
        m = 0
        ls = []
        for i in range(len(l)):
            m = co[l[i]]+m
            ls.append(m)
        ls.pop()
        return sum(ls)
        