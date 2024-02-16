from collections import Counter
class Solution:
    def numberOfWays(self, s: str) -> int:
        count = Counter(s)
        count_1 = count["1"]
        count_0 = count["0"]
        res = 0
        prev0 = 0
        prev1=0
        for i in s:
            if i == "0":
                res += prev1 * (count_1 - prev1)
                prev0+=1
            else:
                res += prev0 * (count_0 - prev0)
                prev1+=1
        return res

        