class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [int(i) for i in range(1,n+1)]
        ind = 0
        while len(friends)>1:
            ind +=k-1
            ind = ind%len(friends)
            friends.pop(ind)
        return friends[0]


