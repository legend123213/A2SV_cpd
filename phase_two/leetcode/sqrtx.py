class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0
        while l <= r:
            mid = l+(r-l)//2
            if mid*mid == x:
                return mid
            if mid*mid>x:
                res = mid
                r = mid -1
            else:
                l = mid +1
        return r

                
        
        