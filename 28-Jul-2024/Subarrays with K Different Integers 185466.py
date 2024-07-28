# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostKDistinct(nums, k) - self.subarraysWithAtMostKDistinct(nums, k - 1)

    def subarraysWithAtMostKDistinct(self, nums, k):
        if k == 0:
            return 0

        i = j = res = 0
        map = {}
        n = len(nums)

        while j < n:
            map[nums[j]] = map.get(nums[j], 0) + 1

            while len(map) > k and i <= j:
                if map[nums[i]] == 1:
                    del map[nums[i]]
                else:
                    map[nums[i]] = map.get(nums[i]) - 1
                
                i += 1

            res += j - i + 1
            j += 1

        return res