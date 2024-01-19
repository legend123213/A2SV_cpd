class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ls = [str(i) for i in nums]
        for i in range(len(ls)):
            for j in range(i+1,len(ls)):
                if ls[i]+ls[j] < ls[j]+ls[i]:
                     ls[i] , ls[j] = ls[j] , ls[i]
        res = "".join(ls)
        if int(res)==0:
            return "0"
        else:
            return res
