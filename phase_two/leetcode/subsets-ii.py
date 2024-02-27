class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        re = []
        def backtrack(ptr,num):
            if ptr>len(nums):
                return
            re.append(num[:])
            for i in range(ptr,len(nums)):
                if i != ptr and nums[i]== nums[i-1]:
                    continue
                num.append(nums[i])
                backtrack(i+1,num)
                num.pop()
        backtrack(0,[])
        return re        