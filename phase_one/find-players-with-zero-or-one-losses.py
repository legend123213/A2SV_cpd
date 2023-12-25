from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = set([k[0] for k in matches])
        los = [k[1] for k in matches]
        wi = win - set(los)
        lo = []
        dic = {}
        Cou = Counter(los)
        for i,val in Cou.items():
            if val==1:
                lo.append(i)

        


        return [sorted(list(wi)),sorted(lo)]
        