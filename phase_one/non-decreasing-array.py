class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        check = 0
        ptr=0
        ptr_f = 1
        p = 0
        while ptr_f<len(nums):
            if nums[ptr]>nums[ptr_f]:
                p=ptr_f
                check+=1
            ptr+=1
            ptr_f+=1
            if check >=2:
                return False
        # print(check)
        k = nums.copy()
        pi = nums.copy()
        k.pop(p)
        pi.pop(p-1)
        # print(k,pi)
        if k != sorted(k) and pi != sorted(pi):
            return False
        
        return True


        