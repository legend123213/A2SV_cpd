class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        count = 0
        k = 0
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                num = stack.pop()
                if num == 0:
                    count = 1
                else:
                    count = num *2
                if not stack:
                    score +=count
                else:
                    stack[-1] += count
        return score
        