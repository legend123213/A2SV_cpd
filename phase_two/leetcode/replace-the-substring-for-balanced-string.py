from collections import Counter,defaultdict
class Solution:
    def balancedString(self, s: str) -> int:
        con = Counter(s)
        num = len(s)//4
        del_s = []
        for i,val in con.items():
            if val<=num:
                del_s.append(i)
        for j in del_s:
            del con[j]
        for i,val in con.items():
            con[i]-=num
        ptr = 0
        ptr_f = 0
        dic = Counter()
        res = float("inf")
        if len(con) == 0:
            return 0
        while ptr_f<len(s):
            dic[s[ptr_f]]+=1
            while len(con-dic) == 0 and ptr<=ptr_f:
                res = min(res,ptr_f-ptr+1)
                dic[s[ptr]]-=1
                ptr+=1
            ptr_f+=1
        return res if res!=float("inf") else 0
        