class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow_co =0
        ls = ['a','e','i','o','u']
        for i in range(k):
            if s[i] in ls:
                vow_co+=1
        ptr=0
        ptr_f=k-1
        maxx = vow_co
        while ptr_f<len(s)-1:
            if s[ptr] in ls:
                vow_co-=1
            if s[ptr_f+1] in ls:
                vow_co+=1
            ptr+=1
            ptr_f+=1
            maxx=max(maxx,vow_co)
        return maxx
        