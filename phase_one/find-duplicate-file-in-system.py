class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        for i in paths:
            path,*files = i.split()
            for filee in files:
                line = filee.split("(")
                ls = [path,"/",line[0]]
                if line[1] in dic:
                    k = dic[line[1]]
                    dic[line[1]] = k+["".join(ls)]
                else:
                    dic[line[1]] = ["".join(ls)]
        res = []
        for founded in dic.values():
            if len(founded)>1:
                res.append(founded)

        return res