from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = dict()
        macc = float("inf")
        for i in range(len(cards)):
            l = dic.setdefault(cards[i], [])
            if len(l)>=1:
                dif= dic[cards[i]][-1]-i
                macc = min(macc,dif*-1)
                dic[cards[i]].append(i)
            else:
                dic.setdefault(cards[i], []).append(i)
        if macc == float("inf"):
            return -1
        return macc+1
            
      