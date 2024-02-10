from collections import Counter
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr_n = 0
        ptr_t = 0
        if name[0]!=typed[0]:
            return False
        while ptr_n<len(name) and ptr_t<len(typed):
            if name[ptr_n]==typed[ptr_t]:
                if ptr_n<len(name):
                    ptr_n+=1
                if ptr_t<len(typed):
                    ptr_t+=1

            else:
                if name[ptr_n-1]==typed[ptr_t]:
                    ptr_t+=1
                else:
                    return False
        while ptr_t<len(typed):
            if name[ptr_n-1]==typed[ptr_t]:
                ptr_t+=1
            else:
                return False
        return ptr_n==len(name) and ptr_t == len(typed)

