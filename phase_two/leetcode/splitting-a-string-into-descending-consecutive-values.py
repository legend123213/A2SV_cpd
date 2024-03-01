class Solution:
    def splitString(self, s: str) -> bool:
        def helper(ptr,ls):
            if ptr >= len(s):
                if len(ls)>=2:
                    return True
                else:
                    return False
            for i in range(ptr,len(s)):
                if not ls or int(ls[-1])-int(s[ptr:i+1]) == 1:
                    ls.append(s[ptr:i+1])
                    res = helper(i+1,ls)
                    ls.pop()
                    if res:
                        return True
            return False
        return helper(0,[])
        


        