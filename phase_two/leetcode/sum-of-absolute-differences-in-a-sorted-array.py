class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        ls = []
        nums.append(0)
        nums.insert(0,0)
        for i in range(1,len(nums)-1):
            front =((i-1)*(nums[i]-nums[i-1])) -  nums[i-1] 
            back = (nums[len(nums)-2]-nums[i])
            no  = (len(nums)-(i+2)) * (nums[i]-nums[i-1])
            real_back = back-no
            ls.append(front+real_back)
        return ls

                

        