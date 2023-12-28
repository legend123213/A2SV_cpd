class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        for i,val in enumerate(nums):
            dic[val]=i
        for op in operations:
            k = dic[op[0]]
            del dic[op[0]]
            dic[op[1]] = k
        return sorted(dic,key =lambda x : dic[x])
        