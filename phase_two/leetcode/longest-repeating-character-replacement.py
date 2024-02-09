from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi  = 0
        ptr = 0
        ptr_f = 0
        max_l = 0
        dic = defaultdict(int)
        while ptr_f<len(s):
            dic[s[ptr_f]]+=1
            maxi = max(maxi,dic[s[ptr_f]])
            while ptr_f-ptr+1-maxi>k:
                dic[s[ptr]]-=1
                ptr+=1
            max_l = max(max_l,ptr_f-ptr+1)
            ptr_f+=1

        return max_l