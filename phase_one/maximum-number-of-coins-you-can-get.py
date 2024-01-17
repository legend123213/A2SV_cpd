class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        ptr = 0
        ptr_l = len(piles)-1
        while ptr_l-ptr>=2:
            res+=piles[ptr_l-1]
            ptr+=1
            ptr_l-=2
        return res