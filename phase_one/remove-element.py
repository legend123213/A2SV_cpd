class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = len(nums)-1
        ptr_f = len(nums)-1
        count=0
        while ptr_f>=0:
            if nums[ptr_f]==val:
                nums[ptr],nums[ptr_f]=nums[ptr_f],nums[ptr]
                ptr-=1
            ptr_f-=1
        return ptr+1


        