class Solution:
    def decodeString(self, s: str) -> str:
        def decode(ptr):
            char =[]
            num = ""
            while ptr<len(s):
                if s[ptr].isdigit():
                    num += s[ptr]
                    
                elif s[ptr] == "[":
                    chars,ptr_re = decode(ptr+1)
                    char.append(chars*int(num))
                    num=""
                    ptr=ptr_re
                    
                elif s[ptr] == "]":
                    break
                else:
                    char.append(s[ptr])
                ptr+=1
            ch = "".join(char)
            return ch,ptr
        return decode(0)[0]