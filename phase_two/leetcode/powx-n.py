class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        def helper(x, n):
            if n == 1:
                return x
            ans = helper(x, n // 2)
            ans *= ans
            if n % 2:
                ans *= x
            return ans
        
        ans = helper(x, abs(n))
        return ans if n >= 0 else 1/ans

        # if n == 0:
        #     return 1.00000
        # if n == 1 or n == -1:
        #     return x
        # if n < 0:
        #     if n%2==0:
        #         ans = self.myPow(x,n//2)**2
        #         print(ans)
        #         return 1/ans
        #     else:
        #         return 1/(x*(self.myPow(x,n//2)**2))
        # else:
        #     if n%2==0:
        #         return (self.myPow(x,n/2)**2)
        #     else:
        #         return x*(self.myPow(x,n//2)**2)
            

            

