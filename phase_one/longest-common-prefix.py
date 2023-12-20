class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptr = 0
        while ptr <= len(strs[0]):
            for j in strs:
                if ptr == len(j):
                    return strs[0][:ptr]
                    break
                if strs[0][ptr] != j[ptr]:
                    return strs[0][:ptr]
                    break
            else:
                ptr+=1
        return strs[0][:ptr]
            

        