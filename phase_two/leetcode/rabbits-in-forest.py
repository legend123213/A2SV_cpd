from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        dic = Counter(answers)
        for i,val in dic.items():
            do_know = (val)%(i+1)
            if do_know ==0:
                res+=val
            else:
                res+=val+(i+1-do_know)
        return res
        

        