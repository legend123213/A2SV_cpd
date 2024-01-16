class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxx,cur = sum(nums[:k]), sum(nums[:k])
        print(cur)
        ptr=0
        ptr_f=k
        while ptr_f<len(nums):
            cur+=(nums[ptr_f]-nums[ptr])
            maxx=max(maxx,cur)
            ptr+=1
            ptr_f+=1
        return maxx/k
