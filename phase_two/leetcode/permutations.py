class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(ptr,num):
            if ptr==len(nums):
                res.append(num[:])
                return 
            
            for i in range(ptr,len(nums)):
                num[i],nums[ptr]= num[ptr],nums[i]
                backtrack(ptr+1,num)
                num[i],num[ptr]=num[ptr],num[i]
            
        backtrack(0,nums)
        return res