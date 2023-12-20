class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x = lambda a : a if a%2==0 else a*2
        return x(n)