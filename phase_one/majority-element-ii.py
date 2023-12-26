from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        con = Counter(nums)
        ls = []
        for i,val in con.items():
            if val > len(nums)//3:
                ls.append(i)
        return ls

        