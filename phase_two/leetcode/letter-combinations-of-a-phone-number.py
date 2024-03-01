class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        def helper(ptr,st):
            if len(st)==len(digits):
                res.append(st[:])
                return 
            for i in dic[digits[ptr]]:
                helper(ptr+1,st+i)
        if len(digits)>0:
            helper(0,"")
        return res


