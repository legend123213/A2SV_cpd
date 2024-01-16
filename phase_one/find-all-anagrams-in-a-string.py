from collections import *
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        j= len(p)
        ls = []
        co = Counter(p)
        d = defaultdict(int)
        if len(p)>len(s):
            return []
        for k in range(len(p)):
            d[s[k]] += 1
        if d==co:
            ls.append(0)
        while j<len(s):
            d[s[i]] -=1
            d[s[j]] +=1
            if  d[s[i]] == 0:
                del d[s[i]]
            if d == co:
                ls.append(i+1)
            i+=1
            j+=1
        return ls

        