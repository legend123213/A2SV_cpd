from collections import defaultdict
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = pow(10,9)+7
        nums.sort(reverse=True)
        ls  = [0]*(len(nums)+1)
        for start,end in requests:
            ls[start]+=1
            ls[end+1]-=1
        for j in range(1,len(ls)):
            ls[j]+=ls[j-1]
        ls.sort(reverse=True)
        res = 0
        for i in range(len(nums)):
            res+=(ls[i]*nums[i])
        return res % MOD
