class Solution:
    def largestOddNumber(self, num: str) -> str:
        rang = -1
        for i in range(len(num)):
            if int(num[i])%2!=0:
               rang = i
            
        return num[:rang+1]