class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        k = sorted(points,key= lambda x:x[1])
        res = -1
        maxx = float("-inf")
        demo = 0
        for i in k:
            if i[0]>maxx:
                maxx = i[1]
                res+=1
        return res+1
        