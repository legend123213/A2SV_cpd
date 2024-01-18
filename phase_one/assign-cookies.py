class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l = min(len(g),len(s))
        g.sort()
        s.sort()
        ptr_g=0
        ptr_s= 0
        counter =0
        while ptr_g<len(g) and ptr_s<len(s):
            if g[ptr_g]<=s[ptr_s]:
                counter+=1
                ptr_s+=1
                ptr_g+=1
            else:
                ptr_s+=1
        return counter
        