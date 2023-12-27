class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ls = []
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                ls.append(fronts[i])
        k  = list(set(fronts+backs) - set(ls))
        l = 0 if len(k)==0 else sorted(k)[0]
        return l
        
        