from collections import defaultdict
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        dic = defaultdict(lambda:-1)
        num = nums+nums
        for i,val in enumerate(num):
            while stack and stack[-1][1]<val:
                nu = stack.pop()
                dic[(nu[0],nu[1])] = val
            stack.append([i%(len(nums)),val])
        dic[stack[0][0]] = stack[0][1]
        return [dic[(i,val)] for i,val in enumerate(nums)]



        