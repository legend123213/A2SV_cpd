class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        ptr_f=0
        while ptr_f<len(nums):
            if nums[ptr_f]!=0:
                nums[ptr],nums[ptr_f] = nums[ptr_f],nums[ptr]
                ptr+=1
            ptr_f+=1
