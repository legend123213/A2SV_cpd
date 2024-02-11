class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        ptr_a = 0
        ptr_b = 0
        while ptr_a<len(firstList) and ptr_b<len(secondList):
            if firstList[ptr_a][1]>=secondList[ptr_b][0] and firstList[ptr_a][0]<=secondList[ptr_b][1]:
                res.append([max(firstList[ptr_a][0],secondList[ptr_b][0]),min(firstList[ptr_a][1],secondList[ptr_b][1])])
            if ptr_a<len(firstList)-1 and ptr_b<len(secondList)-1:
                if firstList[ptr_a][1] < secondList[ptr_b+1][0]:
                    ptr_a+=1
                else:
                    # if firstList[ptr_a][1] == secondList[ptr_b+1][0]:
                    #     res.append([secondList[ptr_b+1][0],secondList[ptr_b+1][0]])
                    ptr_b+=1
                

            else:
                if ptr_a == len(firstList)-1:
                    ptr_b+=1
                else:
                    ptr_a+=1
                    
        return res