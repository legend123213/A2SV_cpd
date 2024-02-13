class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma= nums[0]
        cur = 0
        for i in range(len(nums)):
            if cur<0:
              cur = 0
            cur+=nums[i]
            ma=max(cur,ma)
        return ma