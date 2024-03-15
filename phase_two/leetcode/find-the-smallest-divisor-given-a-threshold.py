class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        res = sum(nums)
        while l<=r:
            mid = l +(r-l)//2
            res = 0
            for i in nums:
                res+=ceil(i/mid)
            if threshold == res:
                res = min(res,mid)
            if res>threshold:
                l = mid+1
            else:
                r = mid -1
        return l
        