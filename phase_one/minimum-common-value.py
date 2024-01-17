class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        k = list(set(nums1) & set(nums2))
        k.sort()
        return k[0] if len(k)!=0 else -1