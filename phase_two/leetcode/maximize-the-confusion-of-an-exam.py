from collections import defaultdict
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ptr = 0
        ptr_f= 0
        maxi = 0
        max_l = 0
        dic = defaultdict(int)
        while ptr_f<len(answerKey):
            dic[answerKey[ptr_f]]+=1
            maxi = max(maxi,dic[answerKey[ptr_f]])
            while (ptr_f-ptr+1)-maxi>k:
                dic[answerKey[ptr]]-=1
                ptr+=1
            max_l = max(max_l,ptr_f-ptr+1)
            ptr_f+=1
        return max_l
        