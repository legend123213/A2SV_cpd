class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]+nums[i]<target:
                    counter+=1
        return counter
        