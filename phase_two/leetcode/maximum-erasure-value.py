from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        conn = defaultdict(int)
        ptr = 0
        ptr_f =0
        summ = 0
        macc = 0
        while ptr_f<len(nums):
            if  not nums[ptr_f] in conn:
                conn[nums[ptr_f]]=1
                summ+=nums[ptr_f]
                ptr_f+=1
                macc = max(macc,summ)
            else:
                if nums[ptr] in conn:
                    del conn[nums[ptr]]
                summ-=nums[ptr]
                
                ptr+=1
        return macc
           


        