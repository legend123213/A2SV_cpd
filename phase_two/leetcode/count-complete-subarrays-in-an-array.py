class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ln = len(set(nums))
        count = 0
        for i in range(len(nums)):
            k = set()
            for j in range(i,len(nums)):
                k.add(nums[j])
                if len(k)==ln:
                    count+=1
        return count