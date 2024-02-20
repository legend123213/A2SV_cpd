class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        sp = nums[0]
        for i in range(1,len(nums)):
            sp+=nums[i]
            if nums[0]<nums[i]:
                res = max(res,ceil((sp)/(i+1)))
            
            
        return res

        