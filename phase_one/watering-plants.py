class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        summ = 0
        for i in range(len(plants)-1):
            print(summ)
            if plants[i] + plants[i+1] <= capacity:
                plants[i+1] = plants[i] + plants[i+1]
            else:
                summ+=(i+1)*2
        summ+=len(plants)
        print(plants)
        return summ
        