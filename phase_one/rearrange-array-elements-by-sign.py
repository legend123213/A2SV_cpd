class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = [x for x in nums if x< 0]
        positive = [y for y in nums if y>0]
        ptr = 0
        ls = []
        while ptr<len(positive):
            ls.append(positive[ptr])
            ls.append(negative[ptr])
            ptr+=1
            
        return ls