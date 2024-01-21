class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ptr=0
        ptr_f=0
        maxx = 0
        k = 1
        while ptr_f<len(nums):
            if nums[ptr_f]==0:
                k-=1
            if k<0:
                if nums[ptr]==0:
                    k+=1
                ptr+=1
            ptr_f+=1
            maxx=max(maxx,ptr_f-ptr)
        return maxx-1
        