from collections import Counter
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        con = Counter(nums)
        con[0]=0
        Max = float('-inf')
        ls = []
        for i in range(len(nums)):
            ls.append(con[0]+con[1])
            Max = max(Max,con[0]+con[1])
            if nums[i]==0:
                con[0]+=1
            else:
                con[1]-=1
        Max = max(Max,con[0]+con[1])
        ls.append(con[0]+con[1])
        l = [i for i in range(len(ls)) if ls[i] == Max]
        return l