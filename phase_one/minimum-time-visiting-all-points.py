class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        ptr = 0
        while ptr < len(points)-1:
            if abs(points[ptr][0] - points[ptr+1][0]) == abs(points[ptr][1] - points[ptr+1][1]):
                distance+=abs(points[ptr][0] - points[ptr+1][0])
            else:
                distance+=max(abs(points[ptr][0] - points[ptr+1][0]),abs(points[ptr][1] - points[ptr+1][1]))
            ptr+=1
        return distance