class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ls = []
        
        ptr = 0
        ptr_f = 1
        p = s[::-1]
        summ = dic[p[0]]
        while ptr_f < len(s):
            if dic[p[ptr]] > dic[p[ptr_f]]:
                summ-=dic[p[ptr_f]]
                ptr+=1
                ptr_f+=1
            else:
                ls.append(summ)
                summ = dic[p[ptr_f]]
                ptr_f+=1
                ptr+=1
        return sum(ls)+summ if list(s) != sorted(s,key = lambda x:dic[x],reverse = True) else sum([dic[x] for x in s])
        