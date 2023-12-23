class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ls = [0]*len(indices)
        for i,val in enumerate(indices):
            ls[val] = s[i]
        return ''.join(ls)