class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        i = 1
        forward = [distance[0]]
        sum_f = distance[0]
        while i < len(distance):
            sum_f+=distance[i]
            i+=1
            forward.append(sum_f)
        res_to_be = forward[destination-1] if start == 0 else abs(forward[destination-1] - forward[start-1])
        print(forward)
        return min(res_to_be,(forward[-1]-res_to_be))