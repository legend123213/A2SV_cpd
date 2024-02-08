from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        tot = 0
        ress= 0
        dic = defaultdict(int)
        dic[0]=1
        for i in nums:
            tot = tot + i
            rem = tot%k
            if rem in dic:
                ress += dic[rem]
            dic[rem]+=1
        return ress


        