class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtracking(ptr,com):
            if ptr>=len(s):
                res.append(com[:])
                return 
            for i in range(ptr,len(s)):
                com.append(s[ptr:i+1])
                if com[-1] == com[-1][::-1]:
                    backtracking(i+1,com)
                com.pop()
        backtracking(0,[])
        return res



        