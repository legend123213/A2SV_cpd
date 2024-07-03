# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)>3:
            ptr = -1
            ptr_2 = 3
            nums.sort()
            res = abs(nums[ptr]-nums[ptr_2])
            for i in range(4):
                res = min(res,abs(nums[ptr]-nums[ptr_2]))
                ptr-=1
                ptr_2-=1
                
            return res
        else:
            return 0


        