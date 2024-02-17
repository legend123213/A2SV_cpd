class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ress = abs(sum(nums[:3])-target)
        cur_summ = sum(nums[:3])
        for i in range(len(nums)):
            ptr = i+1
            ptr_l=len(nums)-1
            while ptr<ptr_l:
                summ = nums[ptr]+nums[ptr_l]+nums[i]
                if summ == target:
                    return summ
                if summ < target:
                    ptr+=1
                else:
                    ptr_l-=1
                dif = abs(target-summ)
                if dif < ress:
                    ress = dif
                    cur_summ = summ

        return cur_summ

                    