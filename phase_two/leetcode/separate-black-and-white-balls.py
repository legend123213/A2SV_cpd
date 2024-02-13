class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        count = 0
        for i in s:
            if i =="1":
                count+=1
            else:
                res+=count
        return res
        