class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(","}":"{","]":"["}
        for i in s:
            if i in [")","}","]"] and len(stack)!=0:
                if dic[i] == stack[-1]:
                    stack.pop()
                    continue
            stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False


                
            stack.append()
        