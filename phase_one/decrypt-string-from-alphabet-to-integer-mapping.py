class Solution:
    def freqAlphabets(self, s: str) -> str:
        al ="abcdefghijklmnopqrstuvwxyz"
        k=""
        ptr=0
        while ptr<len(s)-2:
            if s[ptr+2]=="#":
               k+=al[int(s[ptr:ptr+2])-1]
               ptr+=3
            else:
                k+=al[int(s[ptr])-1]
                ptr+=1
        if ptr == len(s):
            return k 
        else:
            for i in range(ptr,len(s)):
                k+=al[int(s[ptr])-1]
                ptr+=1
            return k

            

                
        