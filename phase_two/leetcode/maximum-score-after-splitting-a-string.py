from collections import Counter
class Solution:
    def maxScore(self, s: str) -> int:
        count_1 = Counter(s)["1"]
        print(count_1)
        count_0 = 0
        macc = 0
        for i in range(len(s)-1):
            if s[i]=="0":
                count_0+=1
            else:
                count_1-=1
                
            macc = max(macc,count_1+count_0)
        return macc

        