class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        re = sum(nums)%p
        tot = 0
        ress= float("inf")
        dic = defaultdict(int)
        dic[0] = -1
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        nums.insert(0,0)
        for i ,j in enumerate(nums):
            dic[j%p] = i
            if (j-re)%p in dic:
                ress = min(ress,i-dic[(j-re)%p])
            
            
            
            
        return ress if ress<len(nums)-1 else -1
        