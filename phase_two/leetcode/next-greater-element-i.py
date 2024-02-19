class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for i in nums2:
            while stack and i > stack[-1] :
                poped_ele = stack.pop()
                dic[poped_ele] = i
            stack.append(i)
        for j in stack:
            dic[j] = -1
        return [dic[num] for num in nums1]
            

        