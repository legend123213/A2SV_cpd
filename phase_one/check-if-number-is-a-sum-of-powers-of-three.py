class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def rec(s,m):
            if s == n:
                return True
            if 3**m>n:
                return False
            add  = s+3**m
            if rec(add,m+1):
                return True
            return rec(s,m+1)
        
        return rec(0,0)