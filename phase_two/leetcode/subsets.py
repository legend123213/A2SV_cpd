class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ls = []
        def back(idx,num):
            if idx>len(nums):
                return
            ls.append(num[:])
            for i in range(idx,len(nums)):
                num.append(nums[i])
                back(i+1,num)
                num.pop()
        back(0,[])
        return ls
        