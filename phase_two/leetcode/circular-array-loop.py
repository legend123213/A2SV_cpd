class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        checked = set()
        for i in range(len(nums)):
            if i not in checked:
                one_cycle_check = set()
                while True:
                    if i in one_cycle_check:
                        return True
                    checked.add(i)
                    one_cycle_check.add(i)
                    prev,i = i,(i+nums[i])%len(nums)
                    if prev == i:
                        break
                    if nums[prev]>0 != nums[i]<0:
                        break
        return False