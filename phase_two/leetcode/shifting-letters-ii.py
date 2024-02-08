class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        k = [0]*(len(s)+1)
        for i in shifts:
            if i[2] == 0:
                k[i[0]]-=1
                k[i[1]+1]+=1
            else:
                k[i[0]]+=1
                k[i[1]+1]-=1
        for i in range(1,len(k)):
            k[i]+=k[i-1]
        res = []
        for j in range(len(s)):
            num = ord(s[j])-97
            st = (num+k[j])%26
            res.append(chr(st+97))
        return "".join(res)

        