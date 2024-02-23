class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = nums[0]
        for i in range(len(nums)):
            if i>maxx:
                return False
            maxx = max(nums[i]+i,maxx)
            if maxx>=len(nums)-1:
                return True
        return False 
        