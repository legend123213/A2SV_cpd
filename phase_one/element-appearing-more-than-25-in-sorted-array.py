from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for key,val in Counter(arr).items():
            if val/len(arr) > 0.25:
                return key
