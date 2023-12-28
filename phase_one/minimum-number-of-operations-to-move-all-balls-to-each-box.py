class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        ind = []
        for i,val in enumerate(boxes):
            if val == "1":
                ind.append(i)
        for i in range(len(boxes)):
            num = 0
            for j in ind:
                num +=abs(j-i)
            res.append(num)
        return res