class Solution:
    def totalMoney(self, n: int) -> int:
        if n<=7:
            return (n*(n+1))//2
        else:
            d = n//7
            r = n%7
            summ = 0
            for i in range(d):
                summ = summ + (7+i)*(7+i+1)//2
                summ =  summ - i*(i+1)//2
            if d !=0:
                t = r+d
                summ = summ + (t*(t+1)//2) - d*(d+1)//2
            return summ
        