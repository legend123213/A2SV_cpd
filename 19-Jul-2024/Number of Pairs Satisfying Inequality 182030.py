# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = []
        for i in range(len(nums1)):
            nums.append(nums1[i]-nums2[i])
        def helper(l,r,ls,co):
            if l == r:
                return [nums[l]],co
            mid = l +(r-l)//2
            le,cr = helper(l,mid,ls,co)
            ri,cl = helper(mid+1,r,ls,co)
            left = 0
            right = 0
            coo = 0
            while left<len(le) and right<len(ri):
                if le[left]-ri[right]<=diff:
                    coo+=len(ri[right:])
                    left+=1
                else:
                    right+=1
            front = 0
            back = 0
            ls = []
            while front<len(le) and back<len(ri):
                if le[front]>=ri[back]:
                    ls.append(ri[back])
                    back+=1
                else:
                    ls.append(le[front])
                    front+=1
            ls.extend(le[front:])
            ls.extend(ri[back:])
            return ls,coo+cl+cr
        res,co = helper(0,len(nums)-1,nums,0)
        return co
