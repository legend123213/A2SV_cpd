from bisect import bisect_left,bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       l = bisect_left(nums,target)
       r = bisect_right(nums,target)-1
       if l == len(nums) or not nums or nums[l] != target:
           return [-1,-1]
       else:
           return[l,r]




