class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ex = list(set(arr1)-set(arr2))
        arr2.extend(sorted(ex))
        arr1.sort(key=lambda k : arr2.index(k) )
        return arr1
        