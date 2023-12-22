class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        nums.insert(0,0)
        maxi = 0
        counter = 0
        for i,v in enumerate(nums):
            if v == 0:
                maxi = max(maxi,counter)
                counter=0
                
            else:
                counter +=1



        return maxi
