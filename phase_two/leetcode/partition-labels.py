class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i,val in enumerate(s):
            dic[val] = i
        size =end = 0
        res = []
        for i,valu in enumerate(s):
            size+=1
            end = max(end,dic[valu]) 
            if i == end:
                res.append(size)
                size = 0
        return res
