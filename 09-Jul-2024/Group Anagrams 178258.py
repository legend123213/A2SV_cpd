# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls = {}
        for i in strs:
            item = i
            p = list(item)
            p = sorted(p)
            p = ''.join(p)
            ls.setdefault(p,[]).append(i)
        res = []
        for key in ls.keys():
            res.append(ls[key]) 
        return res     
        
            
            
                    
        