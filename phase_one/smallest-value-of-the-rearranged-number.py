from collections import Counter
class Solution:
    def smallestNumber(self, num: int) -> int:
        n = list(str(num))
        k = Counter(n)
        if len(n) == 1:
            return int(''.join(n))
        if n[0] == "-":
            i = n.pop(0)
            n.sort(reverse=True)
            n.insert(0,i)
        else:
            n.sort()
            n[0],n[k["0"]]=n[k["0"]],n[0]
        return int(''.join(n))