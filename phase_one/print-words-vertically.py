class Solution:
    def printVertically(self, s: str) -> List[str]:
        k = s.split()
        res = []
        max_s = 0
        r = []
        for string in k:
            max_s = max(len(string),max_s) 
        for i in range(len(k)):
            if len(k[i])<max_s:

                k[i]+= " "*(max_s-len(k[i]))
            res.append(k[i])
        ptr = 0
        while ptr < max_s:
            s = ''
            for letter in res:
                s+=letter[ptr]
            s = s.rstrip()
            r.append(s)
            ptr+=1
        
        return r




        print(res)



        
        