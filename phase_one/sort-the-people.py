class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            maxi =float(-inf)
            ind = -1
            for j in range(i,len(names)):
                if heights[j] > maxi:
                    maxi = heights[j]
                    ind  = j
            if ind != -1:
                names[i],names[ind] = names[ind],names[i]
                heights[i],heights[ind] = heights[ind],heights[i]
        return names

        