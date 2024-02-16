class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        dic = {")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1]==dic[i]:
                    stack.pop()
                    continue
            stack.append(i)
        return len(stack)