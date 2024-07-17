# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr=0
        ptr_f=0
        co = defaultdict(int)
        maxx = 0
        while ptr_f<len(s):
            co[s[ptr_f]]+=1
            while co[s[ptr_f]] >1:
                co[s[ptr]]-=1
                ptr+=1
            maxx = max(maxx,ptr_f-ptr+1)
            ptr_f+=1
        print(maxx)
        return maxx



