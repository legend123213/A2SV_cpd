class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxi = -1
        ptr = 0
        ptr_f = 2
        while ptr_f < len(num):
            if len(list(set(num[ptr:ptr_f+1]))) == 1 and int(num[ptr]) > maxi:
                maxi = int(num[ptr])
                ptr+=3
                ptr_f=ptr+2
            else:
                ptr+=1
                ptr_f+=1
        return str(maxi)*3 if maxi >=0 else ""

        