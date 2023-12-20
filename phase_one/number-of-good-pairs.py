
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num = Counter(nums)
        def addi(n):
            summ = 0
            for i in range(1,n):
                summ+=i
            return summ
        val = 0
        for k,v in num.items():
            val=val+addi(v)

        return val
        
            
            


        