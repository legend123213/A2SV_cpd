class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        if len(names)==1:
            return names
        i = 0
        j = 1
        flag = True
        while True:
            if heights[i] > heights[j]:
                names[i],names[j] = names[j],names[i]
                heights[i],heights[j] = heights[j],heights[i]
                flag = False
            i+=1
            j+=1
            if j == len(heights):
                i = 0
                j = 1
                if flag:
                    return names[::-1]
                else:
                    flag = True
                
                
                    

        