class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        x,y = target
        flag = True
        for pt in ghosts:
            if abs(pt[0]-x)+abs(pt[1]-y) <= abs(x) + abs(y):
                flag = False
                break
            else:
                continue
        return flag

