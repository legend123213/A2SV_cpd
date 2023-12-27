class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ptr=0
        ptr_f=2
        lar = 0
        nums.sort()
        while  ptr_f<len(nums):
            if nums[ptr]+nums[ptr+1] >nums[ptr_f]:
                lar = max(sum(nums[ptr:ptr_f])+nums[ptr_f],lar)
            ptr+=1
            ptr_f+=1
        return lar
        