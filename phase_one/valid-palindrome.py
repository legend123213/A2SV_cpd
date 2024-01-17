class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        s = s.lower()
        strs = ""
        for i in range(len(s)):
            if s[i].isalnum():
                strs = strs + s[i]
        if len(strs) == 0:
            return True
        

        z = len(strs) - 1
        flag = True
        if len(strs) % 2 != 0:
            while z != a:
                if strs[z] != strs[a]:
                    flag = False
                    break
                a += 1
                z -= 1

        else:
            while a - z != 1:
                if strs[z] != strs[a]:
                    flag = False
                    break
                a += 1
                z -= 1
        return flag
        