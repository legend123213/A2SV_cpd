class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls=sorted(nums)
        f=0
        ot=[]
        l=len(nums)-1
        for i in range(len(nums)):
            if ls[f]+ls[l]>target:
                l=l-1
            else:
                if ls[f]+ls[l] == target:
                    break
                else:
                    f=f+1
        for i in range(len(nums)):
            if nums[i] == ls[f] or nums[i]== ls[l]:
                ot.append(i)

        return (ot)
        