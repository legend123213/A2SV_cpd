class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        di = ''.join(digits)
        di = str(eval(di +" + "+"1"))
        res = [int(i) for i in di]
        return res
        