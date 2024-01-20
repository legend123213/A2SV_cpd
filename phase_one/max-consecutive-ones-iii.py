class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ptr = 0
        ptr_f = 0
        l = 0
        maxx = 0
        if k == 0:
            while ptr_f<len(nums) and ptr<len(nums):
                while ptr<len(nums):
                    if nums[ptr]!=0:
                        break
                    ptr+=1
                ptr_f=ptr
                while ptr_f<len(nums):
                    if nums[ptr_f]!=1:
                        break 
                    ptr_f+=1
                maxx=max(maxx,ptr_f-ptr)
                ptr=ptr_f
        else:
            while ptr_f<len(nums)and ptr<=ptr_f:
                while ptr_f<len(nums) and l<=k:
                    if nums[ptr_f]==0 and k==l:
                        break
                    if nums[ptr_f]==0:
                        l+=1
                        ptr_f+=1
                    else:
                        ptr_f+=1
                if nums[ptr]==0:
                    l-=1
                maxx = max(maxx,ptr_f-ptr)
                ptr+=1
        return maxx
                
                
                