class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = l + (r-l)//2
            
            count = 0
            targ = 0
            for i in range(len(weights)-1):
                targ+=weights[i]

                if weights[i+1]+targ > mid or targ == mid:
                    targ = 0
                    count+=1
            
            count+=1
            # print(l,r,count,targ)
            if count > days:
                l = mid+1
            else:
                r = mid 
        return l
        