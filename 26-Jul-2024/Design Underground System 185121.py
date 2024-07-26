# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:
    def __init__(self):
        self.cites = {}
        self.check = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check:
            p = self.check.pop(id)
            if (p[0],stationName) in self.cites:
                tot_t = t - p[1]
                self.cites[(p[0],stationName)][0] += tot_t
                self.cites[(p[0],stationName)][1] += 1
            else:
                self.cites[(p[0],stationName)] = [
                    t - p[1],
                    1,
                ]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return (
            self.cites[(startStation,endStation)][
                0
            ]
            / self.cites[
                (startStation,endStation)
            ][1]
        )


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
