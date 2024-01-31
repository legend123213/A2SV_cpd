class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ptr =-1
        ptr_l = k-1
        ini = sum(cardPoints[0:k])
        kin  = ini
        while ptr>=k*-1:
            ini += cardPoints[ptr]
            ini -= cardPoints[ptr_l]
            ptr-=1
            ptr_l-=1
            kin = max(ini,kin)
        return kin