class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i,val in enumerate(nums):
            for j in range(i,len(nums)):
                if i == j:
                    continue
                if val == nums[j] and (i*j)%k == 0:
                    count+=1
        return count

        