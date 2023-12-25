class Solution:
    

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word = list(words[0]) 
        dic = {}
        ls = []
        for i,val in enumerate(list(order)):
            dic[val] = i
        for i in words:
            li = []
            for j in i:
                li.append(dic[j])
            ls.append(li)
        

        return True if ls == sorted(ls) else False