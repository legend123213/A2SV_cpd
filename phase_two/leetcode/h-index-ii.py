class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations)-1
        
        nums = citations[::-1]
        res = 1 if nums[0]>=1 else 0
        # print(res)
        while l<=r:
            mid = l +(r-l)//2
            if nums[mid]-1>=mid:
                l = mid+1
                res = max(res,l)
            else:
                r = mid-1
        return res