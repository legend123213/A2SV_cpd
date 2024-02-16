from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ls_s = list(count.values())
        ls_s.sort(reverse=True)
        res = 0
        flag = True
        for i in ls_s:
            if i%2!=0:
                i-=1
                flag = False
            res+=i
        return res if flag else res+1

