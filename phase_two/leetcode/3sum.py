class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r]>nums[i]*-1:
                    r-=1
                elif nums[l]+nums[r]<nums[i]*-1:
                    l+=1
                else:
                    if [nums[i],nums[l],nums[r]] not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    r-=1
                    l+=1
            if nums[i]>0:
                break
        return res


        
