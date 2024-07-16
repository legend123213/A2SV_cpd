# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ls = [1]*numOnes
        ls.extend([0]*numZeros)
        ls.extend([-1]*numNegOnes)
        return sum(ls[:k])

        