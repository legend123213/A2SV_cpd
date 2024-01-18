class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ptr_f = 0
        ptr_l = len(nums)-1
        count = 0
        while ptr_l-ptr_f>=1:
            if nums[ptr_f]+nums[ptr_l]==k:
                count+=1
                ptr_f+=1
                ptr_l-=1
            elif nums[ptr_f]+nums[ptr_l]>k:
                ptr_l-=1
            elif nums[ptr_f]+nums[ptr_l]<k:
                ptr_f+=1
        return count
            

        