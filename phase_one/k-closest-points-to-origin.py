from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = defaultdict(int)
        for i in range(len(points)):
            dic[i] = pow(points[i][0],2) + pow(points[i][1],2)
        ls = sorted(dic,key = lambda x:dic[x])
        ls = [points[p] for p in ls[:k]]
        return ls
        