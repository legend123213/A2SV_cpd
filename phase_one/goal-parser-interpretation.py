class Solution:
    def interpret(self, command: str) -> str:
        s =""
        ptr =0
        while ptr<len(command):
            if command[ptr].isalpha():
                s+=command[ptr]
            else:
                if command[ptr] =="(" and command[ptr+1] == ")":
                    s+="o"
            ptr+=1
        return s

        