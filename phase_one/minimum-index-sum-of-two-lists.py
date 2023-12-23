class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        dic = {}
        for i,val in enumerate(list1):
            for j,val2 in enumerate(list2):
                if val == val2:
                    dic[val] = i+j
        mini = min(dic.values())
        for k,v in dic.items():
            if v == mini:
                res.append(k)
        return res


        