class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_e = -1
        min_e = float("inf")
        for i in range(len(trips)):
            max_e = max(max_e,trips[i][2])
            min_e = min(min_e,trips[i][1])
        ls = [0]*(1+max_e+min_e)
        for j in range(len(trips)):
            ls[trips[j][1]]+= trips[j][0]
            ls[trips[j][2]]-=trips[j][0]
        for s in range(1,len(ls)):
            ls[s]+=ls[s-1]
        max_camp = max(ls)
        if capacity<max_camp:
            return False
        
        return True


        

            
        