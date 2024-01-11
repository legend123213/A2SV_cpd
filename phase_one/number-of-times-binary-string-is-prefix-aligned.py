class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        top = 0
        count = 0
        for i in range(len(flips)):
            flips[i] +=top
            top = flips[i]
        for i in range(len(flips)+1):
            if (i*(i+1))//2 == flips[i-1]:
                count+=1
        return count         