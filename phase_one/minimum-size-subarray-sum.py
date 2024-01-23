class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minn = float('+inf')
        ptr = 0
        ptr_f = 0
        summ = 0
        while ptr_f<len(nums):
            if summ+nums[ptr_f]>=target:
                minn=min(minn,ptr_f-ptr+1)
                summ-=nums[ptr]
                ptr+=1
            else:
                summ+=nums[ptr_f]
                ptr_f+=1
        return minn if minn!=float('+inf') else 0
        