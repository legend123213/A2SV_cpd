class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1]== nums[i]:
                nums[i-1]*=2
                nums[i]=0
        ptr_p=0
        ptr_s=1
        while ptr_s<len(nums) and ptr_p<len(nums):
            if nums[ptr_p] != 0:
                ptr_p+=1
                ptr_s = ptr_p+1
            elif nums[ptr_s] ==0:
                ptr_s+=1
            else:
                nums[ptr_p],nums[ptr_s] =  nums[ptr_s],nums[ptr_p]
                ptr_p += 1
                ptr_s += 1
        return nums

        