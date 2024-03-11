class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lormin = 1
        rormax = max(piles)
        while lormin < rormax:
            mid = lormin + (rormax - lormin)//2
            changer  = 0
            for i in piles:
                changer+= i//mid
                if i % mid !=0:
                    changer+=1
            if changer <= h:
                rormax=mid
            else:
                lormin = mid +1
        return lormin      