class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        dic = {}
        res=[0]*len(temperatures)
        ls = 0
        for i,val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                k= stack.pop()
                res[k[1]] = i-k[1]
            stack.append([val,i])
        return res