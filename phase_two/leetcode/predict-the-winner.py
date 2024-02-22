class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(l,r):
            if r == l:
                return nums[r]
            left = nums[l]-rec(l+1,r)
            right = nums[r]-rec(l,r-1)
            return max(right,left)
        return True if rec(0,len(nums)-1) >=0 else False