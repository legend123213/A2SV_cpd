class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nu = ["1","2","3","4","5","6","7","8","9"]
        res = []
        for i in range(len(nu)):
            ls = [nu[i]]
            for j in range(i+1,len(nu)):
                ls.append(nu[j])
                k=int("".join(ls))
                if k <= high and k >=low:
                    res.append(k)
        return sorted(res)

        