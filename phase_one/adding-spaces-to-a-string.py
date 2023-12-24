class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        k = list()
        ptr = 0
        ptr_s = 0
        while ptr_s<len(spaces):
            if ptr == spaces[ptr_s]:
                k.append(" ")
                k.append(s[ptr])
                ptr_s+=1
            else:
                k.append(s[ptr])
            ptr+=1
        p = list(s[ptr::])
        k.extend(p)
        return "".join(k)