class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        num = [0]*(n+1)
        for i in bookings:
            num[i[0]-1]+=i[2]
            num[i[1]]-=i[2]
        for j in range(1,len(num)):
            num[j]+=num[j-1]
        num.pop()
        return num
        