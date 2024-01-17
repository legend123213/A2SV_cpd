class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        maxx = 0
        for i in range(len(processorTime)):
            maxx = max(maxx,processorTime[i]+tasks[len(tasks)-(i*4)-1])
        return maxx