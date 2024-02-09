from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ptr = 0
        ptr_f = 0
        maxi = 0
        summ = 0
        dic = defaultdict(int)
        while ptr_f<len(fruits):
            dic[fruits[ptr_f]] +=1
            summ +=  fruits[ptr_f]
            while len(dic)>2:
                dic[fruits[ptr]]-=1
                if dic[fruits[ptr]] == 0:
                   del dic[fruits[ptr]]
                summ-=fruits[ptr]
                ptr+=1
            maxi = max(maxi,ptr_f-ptr+1)
            ptr_f+=1
        return maxi





        