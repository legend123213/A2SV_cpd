class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        k = maxDoubles
        counter = 0
        t = target
        while t>1:
            if t%2!=0:
                t-=1
                counter+=1
            else:
                if k>0:
                    counter+=1
                    t=t//2
                    k-=1
                else:
                    counter+=t-1
                    t = 0
        return counter

        