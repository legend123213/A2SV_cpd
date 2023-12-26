class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ptr = 0
        ptr_f = 1
        ls = []
        while ptr_f <len(nums):
            ls.extend([nums[ptr_f]]*nums[ptr])
            ptr+=2
            ptr_f+=2
        return ls

        