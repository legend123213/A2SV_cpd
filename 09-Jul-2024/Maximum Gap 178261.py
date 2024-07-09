# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1,len(nums)):
            res = max(res,nums[i]-nums[i-1])
        if len(nums)<2:
            return 0
        return res