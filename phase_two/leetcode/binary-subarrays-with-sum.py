from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = defaultdict(int)
        res = 0
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        nums.insert(0,0)
        for num in nums:
            if num-goal in dic:
                res+=dic[num-goal]
            dic[num]+=1
        return res
            
