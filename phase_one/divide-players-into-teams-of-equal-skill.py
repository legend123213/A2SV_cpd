class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r = 0 ,len(skill)-1
        flag = True
        tester =skill[l]+skill[r]
        res = 0
        while l<=r:
            if skill[l]+skill[r]==tester:
                res=res+skill[l]*skill[r]
                l+=1
                r-=1
            else:
                flag = False
                break
        


        return res if flag else -1
        