class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        su = 0
        ls = []
        for i in costs:
            su+=i
            if su > coins:
                break
            ls.append(su)
        return len(ls)
        