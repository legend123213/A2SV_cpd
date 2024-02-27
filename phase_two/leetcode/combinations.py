class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def recuHelper(j,num):
            if len(num) == k:
                res.append(num[:])
                return 
            for i in range(j,n+1):
                num.append(i)
                recuHelper(i+1,num)
                num.pop()
        recuHelper(1,[])
        return res

            