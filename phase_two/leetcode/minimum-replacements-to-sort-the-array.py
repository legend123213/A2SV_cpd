class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        minn = nums[0]
        opr = 0
        nums = nums[::-1]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                demo = ceil(nums[i]/nums[i-1])
                nums[i] = nums[i]//demo
                opr += demo-1
        return opr
        