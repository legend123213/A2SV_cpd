class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        k = ["*","/","-","+"]
        ls = []
        res = 0
        for i in range(len(tokens)):
            if tokens[i] in k:
                m=ls.pop()
                n=ls.pop()
                res =int(eval(n + tokens[i] +m))
                ls.append(str(res))
            else:
                ls.append(tokens[i])
        
        return int(ls[-1])

        