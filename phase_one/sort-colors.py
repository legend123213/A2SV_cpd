from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = Counter(nums)
        ls = [0,1,2]
        ptr = 0
        ptr_f=0
        for i,val in enumerate(ls):
            while ptr_f<len(nums):
                if nums[ptr_f] == ls[i]:
                    nums[ptr],nums[ptr_f] = nums[ptr_f],nums[ptr]
                    ptr+=1
                ptr_f+=1
            ptr = dic[i]
            ptr_f = dic[i]
            if i == 1:
                break
        return nums

        