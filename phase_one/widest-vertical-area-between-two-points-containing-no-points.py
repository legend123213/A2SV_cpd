class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ma = float('-inf')
        for i in range(1,len(points)):
            ma = max(ma,points[i][0] - points[i-1][0])
        return ma
        